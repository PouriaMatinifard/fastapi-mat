from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func
from ..database import get_db
from .. import models, schemas, oauth2
from typing import List, Optional

router = APIRouter(
    prefix="/posts",
    tags=["posts"]
)

#@router.get("/", status_code = status.HTTP_200_OK, response_model = List[schemas.PostResp])

@router.get("/", status_code = status.HTTP_200_OK, response_model = List[schemas.PostOutVote])
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user),
              limit: int = 10, skip: int = 0, search: Optional[str] = ""):

    #posts =db.query(models.Post).all()

    #posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

    results = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).\
        join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).\
        filter(models.Post.title.contains(search)).limit(limit).offset(skip)

    results = results.all()

    '''if models.Post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="not authorized"
                                                                          "for the requested command")'''
    return results


#3
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.PostResp)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int =
                 Depends(oauth2.get_current_user)):


    #print(current_user)
    new_post = models.Post(owner_id=current_user.id, **post.dict())#new_post = models.Post(title=post.title,.......)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post

#6
#@router.get("/{id}", response_model = schemas.PostResp)
@router.get("/{id}", response_model = schemas.PostOutVote)
def get_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    #post1 = db.query(models.Post).filter(models.Post.id == id).first()

    post1 = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).\
        join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).\
        filter(models.Post.id == id).first()


    if not post1:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
                            detail=f"the post with id {id} does not exist!")

    '''if models.Post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="not authorized for the desired request!")'''

    return post1

#8
@router.delete("/delpost/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):


    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail=f"the post with the id {id} does not exist baby")

    '''if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="not authorized"
                                                                          "for the requested command")'''

    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

#10
@router.put("/posts/updates/{id}", status_code = status.HTTP_205_RESET_CONTENT, response_model = schemas.PostResp)
def update_post(id: int, post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int =
                 Depends(oauth2.get_current_user)):

    '''cursor.execute("UPDATE posts SET title = %s,content= %s,published= %s WHERE id= %s returning *",
                   (post.title, post.content,post.published, str(id)))
    updated_post=cursor.fetchone()
    cnx.commit()'''

    post_query = db.query(models.Post).filter(models.Post.id == id)

    post1 = post_query.first()

    if post1 == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"the post with the id {id} does not exist baby")

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="not authorized"
                                                                          "for the requested command")

    post_query.update(post.dict(), synchronize_session=False)
    db.commit()
#11
    return post_query.first()
