import face_recognition

def are_same_person(image1, image2):
    image1_data = face_recognition.load_image_file(image1)
    image2_data = face_recognition.load_image_file(image2)

    face_encoding1 = face_recognition.face_encodings(image1_data)
    face_encoding2 = face_recognition.face_encodings(image2_data)

    if not face_encoding1 or not face_encoding2:
        return False

    result = face_recognition.compare_faces([face_encoding1[0]], face_encoding2[0])
    return result[0]