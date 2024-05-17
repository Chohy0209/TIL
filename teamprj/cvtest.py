# import cv2
# import numpy as np

# # 눈 내리는 효과 추가
# # def add_snow(frame):
# #     # 화면 크기에서 눈의 개수 계산
# #     num_snowflakes = int(frame.shape[1] * frame.shape[0] / 10000)
    
# #     # 눈의 위치와 크기를 랜덤하게 생성
# #     snowflakes = [(np.random.randint(0, frame.shape[1]), np.random.randint(0, frame.shape[0]), np.random.randint(2, 5), np.random.randint(5, 10)) for _ in range(num_snowflakes)]

# #     # 눈 그리기
# #     for (x, y, radius, speed) in snowflakes:
# #         cv2.circle(frame, (x, y), radius, (146, 214, 244), -1)
# #         y += speed
# #         if y > frame.shape[0]:
# #             y = 0

# #     return frame

# def add_sand(frame):  
#     num_particles = int(frame.shape[1] * frame.shape[0] / 10000)  
#     particles = [(np.random.randint(0, frame.shape[1]), np.random.randint(0, frame.shape[0]), np.random.randint(1, 2), np.random.randint(1, 3)) for _ in range(num_particles)]


#     for i, (x, y, radius, speed) in enumerate(particles):
            
#             cv2.circle(frame, (x, y), radius, (120,120,120), -1)
#             y += speed
#             if y > frame.shape[0]:
#                 y = 0
#             x += np.random.randint(-1, 2)  
#             if x > frame.shape[1]:
#                 x = 0
#             elif x < 0:
#                 x = frame.shape[1]
#     return frame
# # 동영상 프레임 생성
# def create_frames():
#     while True:
#         # 배경 생성
#         background = cv2.imread("C:/Users/master/cli/TIL/teamprj/img/foggyday.jpg")  # 이미지A.png를 사용하여 배경 생성
#         background = cv2.resize(background, (1280, 720))  # 이미지 크기를 1280x720으로 조정

#         #눈 내리게 하기
#         snow_background = add_sand(background)

#         yield snow_background

# # 동영상 저장
# def save_video():
#     frame_generator = create_frames()
#     fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#     out = cv2.VideoWriter('foggy kyeongbok.mp4', fourcc, 30.0, (1280, 720))

#     for _ in range(300):  # 10초 분량
#         frame = next(frame_generator)
#         out.write(frame)
    
#     out.release()

# if __name__ == "__main__":
#     save_video()
# # import cv2
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




# import cv2
# import numpy as np

# def add_sand(frame):  
#     num_particles = int(frame.shape[1] * frame.shape[0] / 10000)  # 더 많은 입자를 생성하여 더 밀집한 모래 효과를 만듦
#     particles = [(np.random.randint(0, frame.shape[1]), np.random.randint(0, frame.shape[0]), np.random.randint(1, 2), np.random.randint(1, 3)) for _ in range(num_particles)]
    
    
#     # 모래색의 범위를 설정 랜덤하게 연한 갈색 사이에서 선택됨
#     sand_colors = [(np.random.randint(160, 180), np.random.randint(110, 130), np.random.randint(50, 70)) for _ in range(num_particles)]



    
#     for i, (x, y, radius, speed) in enumerate(particles):
#         sand_color = sand_colors[i]
#         cv2.circle(frame, (x, y), radius, sand_color, -1)
#         y += speed
#         if y > frame.shape[0]:
#             y = 0
#         x += np.random.randint(-1, 2)  
#         if x > frame.shape[1]:
#             x = 0
#         elif x < 0:
#             x = frame.shape[1]
#     return frame


# # 동영상 프레임 생성
# def create_frames():
#     while True:
#         background = cv2.imread("C:/Users/master/cli/TIL/teamprj/img/sandstorm.jpg")
#         background = cv2.resize(background, (1280, 720))  
#         sand_background = add_sand(background)
#         yield sand_background

# # 동영상 생성 및 저장
# height, width, _ = cv2.imread("C:/Users/master/cli/TIL/teamprj/img/sandstorm.jpg").shape
# fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
# video = cv2.VideoWriter('sandstorm_effect_video.mp4', fourcc, 30.0, (width, height))

# frame_generator = create_frames()

# for _ in range(100):  
#     frame = next(frame_generator)
#     video.write(frame)

# video.release()

import cv2
import numpy as np
import time  # 시간 지연을 위한 모듈 추가

# 이미지 파일 경로
image_path = "img/k_clear.jpg"

# 이미지 읽기
background = cv2.imread(image_path)

# 이미지 크기 가져오기
image_height, image_width, _ = background.shape

# 구름 색상 설정 (흰색)
cloud_color = (255, 255, 255)

# 이동 속도 설정
move_speed = 5

# 구름 세트를 그리는 함수
def draw_cloud_set(frame, cloud_x, cloud_y):
    # 가로로 긴 구름
    # 첫 번째 원
    cv2.ellipse(frame, (cloud_x - 30, cloud_y), (40, 20), 0, 0, 360, cloud_color, -1)
    # 두 번째 원
    cv2.ellipse(frame, (cloud_x + 30, cloud_y), (40, 20), 0, 0, 360, cloud_color, -1)
    
    # 세로로 짧은 구름
    # 첫 번째 원
    cv2.ellipse(frame, (cloud_x - 30, cloud_y + 20), (40, 20), 0, 0, 360, cloud_color, -1)
    # 두 번째 원
    cv2.ellipse(frame, (cloud_x + 30, cloud_y + 20), (40, 20), 0, 0, 360, cloud_color, -1)
    
    # 추가 구름 부분
    cv2.ellipse(frame, (cloud_x + 55, cloud_y + 10), (55, 20), 0, 0, 360, cloud_color, -1)
    cv2.ellipse(frame, (cloud_x - 55, cloud_y + 10), (55, 20), 0, 0, 360, cloud_color, -1)

# 초기 구름 위치 리스트 설정
cloud_positions = [
    (image_width + 100, 50),
    (image_width + 250, 150),
    (image_width + 400, 250),
    (image_width + 550, 100),
    (image_width + 700, 200),
    (image_width + 850, 30),
    (image_width + 1000, 150),
    (image_width + 1150, 250),
    # (image_width + 1300, 100),
    # (image_width + 1450, 200)
]

# 무한 루프
while True:
    # 이미지 복사
    frame = background.copy()
    
    # 구름 세트 그리기
    for i, (cloud_x, cloud_y) in enumerate(cloud_positions):
        draw_cloud_set(frame, cloud_x, cloud_y)
        # 구름 왼쪽으로 이동
        cloud_positions[i] = (cloud_x - move_speed, cloud_y)
        # 구름이 왼쪽 끝으로 이동하기 전에 다시 오른쪽 끝에서 나타나도록 설정
        if cloud_positions[i][0] < -200:  # 구름이 완전히 사라진 후에만 cloud_x를 초기화
            cloud_positions[i] = (image_width + 100, cloud_y)

    # 이미지 화면에 표시
    cv2.imshow("Moving Clouds", frame)
    
    # 화면 업데이트
    cv2.waitKey(30)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 윈도우 종료
cv2.destroyAllWindows()

# 동영상 저장
def save_video():
    frame_generator = create_frames()
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('clear_kyeongbok.mp4', fourcc, 30.0, (1280, 720))

    frame_count = 0  # 생성한 프레임 수를 추적하기 위한 변수 추가
    max_frames = 300  # 생성할 최대 프레임 수 설정

    for frame in frame_generator:
        out.write(frame)
        frame_count += 1
        if frame_count >= max_frames:  # 최대 프레임 수에 도달하면 루프 종료
            break
    
    out.release()

if __name__ == "__main__":
    save_video()


# import cv2
# import numpy as np

# def add_sunshine_effect(image):
#     # 이미지의 중심을 기준으로 광선 효과를 생성합니다.
#     center_x, center_y = image.shape[1] // 2, image.shape[0] // 2
    
#     # 빛이 비추는 지점의 반지름을 설정합니다.
#     radius = min(center_x, center_y) // 2

#     # 빛이 비추는 지점을 표현하는 원을 생성합니다.
#     mask = np.zeros_like(image)
#     cv2.circle(mask, (center_x, center_y), radius, (255, 255, 255), -1)
    
#     # 원을 흐리게(blur) 처리하여 부드러운 광선 효과를 생성합니다.
#     blurred_mask = cv2.GaussianBlur(mask, (radius // 3, radius // 3), 0)

#     # 이미지에 광선 효과를 추가합니다.
#     alpha = 0.2  # 효과의 강도를 조절합니다.
#     sun_effect = cv2.addWeighted(image, 1, blurred_mask, alpha, 0)

#     return sun_effect

# # 이미지 불러오기
# image = cv2.imread("C:/Users/master/cli/TIL/teamprj/img/clear kyeongbok.jpg")

# # 광선 효과 추가
# image_with_sunshine = add_sunshine_effect(image)

# # 결과 이미지를 화면에 표시
# cv2.imshow("Sunshine Effect", image_with_sunshine)
# cv2.waitKey(0)
# cv2.destroyAllWindows()