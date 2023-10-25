from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt
from models import User
from schemas import UserSchema


user_bp = Blueprint("users", __name__)


@user_bp.get("/all")
@jwt_required()
def get_all_users():
   # claims = get_jwt()

    #if claims.get("is_staff") == True:
        page = request.args.get("page", default=1, type=int)

        per_page = request.args.get("per_page", default=3, type=int)

        users = User.query.paginate(page=page, per_page=per_page)

        result = UserSchema().dump(users, many=True)

        return (
            jsonify(
                {
                    "users": result,
                }
            ),
            200,
        )

   # return jsonify({"message": "You are not authorized to access this"}), 401

@user_bp.put("/updateEmail")
@jwt_required()
def update_email_id():
    data = request.get_json()
    current_user = User.get_user_by_username(username=data.get("username"))
    if current_user is None:
        return jsonify({"error": "User name incorrect"}), 409
    old_email = current_user.email
    current_user.email = data.get("email")
    current_user.commit()
    return jsonify({
        "message": "Email updated successfully",
        "old email": old_email,
        "updated email": current_user.email
    }, 200)


@user_bp.delete("/deleteFitnessAccount")
@jwt_required()
def delete_fit_account():
    data = request.get_json()
    current_user = User.get_user_by_username(username=data.get("username"))
    if current_user is None:
        return jsonify({"error": "User name incorrect"}), 409
    current_user.delete()
    return jsonify({
        "message": "Account deleted"
    }, 204)



