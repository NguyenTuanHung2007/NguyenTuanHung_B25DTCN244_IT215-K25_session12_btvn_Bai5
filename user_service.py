from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from models import DiscountModel
from datetime import datetime

def delete_discount_service(db: Session, discount_id: int):
    discount = db.query(DiscountModel).filter(
        DiscountModel.id == discount_id, 
        DiscountModel.is_deleted == False
    ).first()
    
    if not discount:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Mã giảm giá không tồn tại hoặc đã bị xóa trước đó"
        )
    
    if discount.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Không thể xóa mã giảm giá đang trong trạng thái hoạt động. Vui lòng tắt kích hoạt trước."
        )
    
    discount.is_deleted = True
    discount.deleted_at = datetime.now()
    
    db.commit()
    db.refresh(discount)
    
    return discount