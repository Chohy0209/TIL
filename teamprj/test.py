#처음 배경이미지 불러오기위한 cap지정
cap = cv2.VideoCapture(weather.image_path) #영상을 가져와서 cap에 저장
ret, frame = cap.read() #cap 에서 frame이 제대로 읽어졌으면 ret은 True 아니면 False가 됨, 이미지는 frame 에 읽음

#이 밑에부터는 while문 안으로 들어가야함
frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
frame_pygame = pg.image.frombuffer(frame_rgb.tobytes(), frame_rgb.shape[:2][::-1], "RGB") #frame에 담겨있는 이미지파일을 pygame 화면에 맞게 바꿈

frame_pygame=pg.transform.scale(frame_pygame, (self.data_indices[1][-1][-1]+96, self.data_indices[0][-1][-1]+96)) #변환한 비디오 frame 이미지를 맵 사이즈에 맞게 리사이징
WINDOW.blit(frame_pygame, (self.bg_x - CURR_CHAR.pull_x, self.bg_y - CURR_CHAR.pull_y)) #파이게임 화면에 그리기
ret, frame = cap.read() #다음 순서의 화면 불러오기
if not ret: #다음 순서화면이 없으면(영상이 끝나면) ret이 False면 다음 frame이미지가 제대로 읽어지지않은것.
    cap.set(cv2.CAP_PROP_POS_FRAMES, 3) #cap을 3번째 컷으로 옮겨서 읽음
    ret, frame = cap.read()