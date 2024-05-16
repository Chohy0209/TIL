import cv2
import numpy as np

# 눈 내리는 효과 추가
def add_snow(frame):
    # 화면 크기에서 눈의 개수 계산
    num_snowflakes = int(frame.shape[1] * frame.shape[0] / 8000)
    
    # 눈의 위치와 크기를 랜덤하게 생성
    snowflakes = [(np.random.randint(0, frame.shape[1]), np.random.randint(0, frame.shape[0]), np.random.randint(2, 5), np.random.randint(10, 20)) for _ in range(num_snowflakes)]

    # 눈 그리기
    for (x, y, radius, speed) in snowflakes:
        cv2.circle(frame, (x, y), radius, (255, 255, 255,1), -1)
        y += speed
        if y > frame.shape[0]:
            y = 0

    return frame

# 동영상 프레임 생성
def create_frames():
    while True:
        # 배경 생성
        background = cv2.imread("C:/Users/master/cli/TIL/teamprj/img/snow gyeongbok.jpg")  # 이미지A.png를 사용하여 배경 생성
        background = cv2.resize(background, (1280, 720))  # 이미지 크기를 1280x720으로 조정

        #눈 내리게 하기
        snow_background = add_snow(background)

        yield snow_background

# 동영상 저장
def save_video():
    frame_generator = create_frames()
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('snowy_cartoon_background.mp4', fourcc, 30.0, (1280, 720))

    for _ in range(300):  # 10초 분량
        frame = next(frame_generator)
        out.write(frame)
    
    out.release()

if __name__ == "__main__":
    save_video()
# import cv2
# import numpy as np

# # 비를 그리는 함수
# def draw_rain(frame):
#     # 비의 개수 및 위치 설정
#     num_raindrops = 20
#     for _ in range(num_raindrops):
#         # 비의 랜덤한 시작점과 종료점 설정
#         start_point = (np.random.randint(0, frame.shape[1]), np.random.randint(0, frame.shape[0]))
#         end_point = (start_point[0] + np.random.randint(-10, 10), start_point[1] + np.random.randint(10, 30))
#         # 비의 색상 (파란색)
#         thickness = np.random.randint(1, 3)
#         color = (0, 0, 0, 1)
#         # 선 그리기
#         cv2.line(frame, start_point, end_point, color, thickness)

#     return frame

# # 비 효과를 추가한 프레임 생성
# def create_frames():
#     while True:
       
#         background = cv2.imread("C:/Users/master/cli/TIL/teamprj/img/rainn.jpg")
#         background = cv2.resize(background, (1280, 720))
#         # 비 효과 추가
#         rain_background = draw_rain(background)
        
#         yield rain_background

# # 동영상 저장
# def save_video():
#     frame_generator = create_frames()
#     fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#     out = cv2.VideoWriter('rainy_effect.mp4', fourcc, 30.0, (1280, 720))

#     for _ in range(300):  # 10초 분량
#         frame = next(frame_generator)
#         out.write(frame)
    
#     out.release()

# if __name__ == "__main__":
#     save_video()

