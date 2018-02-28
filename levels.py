levels = []
levelSprites = []

levels.append([ \
    bytearray(b'YYYYYYYYYYY                 YYY'), \
    bytearray(b'XXXXXXXXXXX                 YYY'), \
    bytearray(b'\x1e\x1e_`abc\x1e\x1e\x1e\x1e     !           YYY'), \
    bytearray(b'\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e                 XXX'), \
    bytearray(b'e!        e     $       gg  \x1eV\x1e'), \
    bytearray(b'f         d  &&&&&&&&       \x1eW\x1e'), \
    bytearray(b'f                           \x1e\x1e\x1e'), \
    bytearray(b'd                           \x1eV\x1e'), \
    bytearray(b'\x1egjjjjggggegg       $       \x1eW\x1e'), \
    bytearray(b'\x1e         f       gg\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e'), \
    bytearray(b'\x1e jjj     f  ggg    \x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e'), \
    bytearray(b'\x1e         f         \x1eVV\x1e\x1eVV\x1eVV\x1e'), \
    bytearray(b'\x1e jjj     f!   ggg  \x1eWW\x1e\x1eWW\x1eWW\x1e'), \
    bytearray(b'\x1e         f          %  \x1e\x1e\x1e\x1e\x1e\x1e\x1e'), \
    bytearray(b'\x1e jjj     f   ggg    !  \x1e\x1e\x1e\x1e\x1e\x1e\x1e'), \
    bytearray(b'\x1e%      ! f             \x1eVV\x1eVV\x1e'), \
    bytearray(b'\x1eNNNNNNN\x1e\x1ef  ggg        \x1eWW\x1eWW\x1e'), \
    bytearray(b'\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1ed             \x1e\x1e\x1e\x1e\x1e\x1e\x1e'), \
    bytearray(b'\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e')])

levels.append([ \
    bytearray(b'\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e'), \
    bytearray(b'\x1e           !     \x1e\x1e\x1e\x1e\x1e      \x1e\x1e'), \
    bytearray(b'\x1e                  \x1e\x1e\x1e        \x1e'), \
    bytearray(b'\x1egg                 \x1e       ! \x1e'), \
    bytearray(b'\x1e          jjj                \x1e'), \
    bytearray(b'\x1e                             \x1e'), \
    bytearray(b'\x1eNNNNNNNNNNNNNNNNNNNNN        \x1e'), \
    bytearray(b'\x1e                        jjjjj\x1e'), \
    bytearray(b'\x1e     \x1e                     \x1e\x1e\x1e'), \
    bytearray(b'\x1e     \x1ejjjjjjjjjggggg         \x1e'), \
    bytearray(b'\x1ejjjjj! % % % %         gggg  \x1e'), \
    bytearray(b'\x1e                           ! \x1e'), \
    bytearray(b'\x1e                             \x1e'), \
    bytearray(b'\x1eNNNNNNNN     jjjjjj    ggg   \x1e'), \
    bytearray(b'\x1e!        jj                  \x1e'), \
    bytearray(b'\x1e         jj  gg             \x1e\x1e'), \
    bytearray(b'\x1e                 gg          \x1e'), \
    bytearray(b'\x1e                             \x1e'), \
    bytearray(b'\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e')])

levels.append([ \
    bytearray(b'\x1e\x1e\x1e\x1e\x1e   %   %    \x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e'), \
    bytearray(b'\x1e        !                    \x1e'), \
    bytearray(b'\x1e                             \x1e'), \
    bytearray(b'\x1e                          \x1e  \x1e'), \
    bytearray(b'\x1e                     gggjje  \x1e'), \
    bytearray(b'\x1egggjjjjjjjjjjjjjjjjj   %! f  \x1e'), \
    bytearray(b'\x1e                   gg  ejjf  \x1e'), \
    bytearray(b'\x1e\x1e\x1e\x1e\x1e                  !fjjf  \x1e'), \
    bytearray(b'\x1e!                gg    fjjf  \x1e'), \
    bytearray(b'\x1e     gggg              fjjf  \x1e'), \
    bytearray(b'\x1e                   gg  fjjf  \x1e'), \
    bytearray(b'\x1eNNNNNN         !       fjjf  \x1e'), \
    bytearray(b'\x1e         jjjjj       ggfjjf  \x1e'), \
    bytearray(b'\x1e                       fjjf  \x1e'), \
    bytearray(b'\x1e           &&&&        fjjf  \x1e'), \
    bytearray(b'\x1e\x1f\x1f\x1f              gg    djjd  \x1e'), \
    bytearray(b'\x1e               jjjj          \x1e'), \
    bytearray(b'\x1e                             \x1e'), \
    bytearray(b'\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e')])

levels.append([ \
    bytearray(b'\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e'), \
    bytearray(b'\x1e                    !        \x1e'), \
    bytearray(b'\x1e                             \x1e'), \
    bytearray(b'\x1ejjjj  jjjjj  gg    gg        \x1e'), \
    bytearray(b'\x1e             % NN            \x1e'), \
    bytearray(b'\x1ejj           \x1e   NN        gg\x1e'), \
    bytearray(b'\x1e           jj\x1e          $    \x1e'), \
    bytearray(b'\x1ejj           \x1e      &\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e'), \
    bytearray(b'\x1e       $     \x1e    &&  %      \x1e'), \
    bytearray(b'\x1e\x1e\x1e&&&&&&&&&&&\x1e  && !         \x1e'), \
    bytearray(b'\x1e       !     \x1e               \x1e'), \
    bytearray(b'\x1e             \x1eN              \x1e'), \
    bytearray(b'\x1e             \x1e        gg     \x1e'), \
    bytearray(b'\x1egg\x1e     NNN\x1e\x1e\x1eggg           g\x1e'), \
    bytearray(b'\x1e  \x1e          \x1e             gg\x1e'), \
    bytearray(b'\x1ej \x1eNNNNNNNN  \x1e            gg%\x1e'), \
    bytearray(b'\x1e                         gg%%\x1e'), \
    bytearray(b'\x1ej                       gg%%%\x1e'), \
    bytearray(b'\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e')])

levels.append([ \
    bytearray(b'\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e'), \
    bytearray(b'\x1e                    !        \x1e'), \
    bytearray(b'\x1e                             \x1e'), \
    bytearray(b'\x1e*jjj  jjjjj  gg    gg        \x1e'), \
    bytearray(b'\x1e*            % NN           *\x1e'), \
    bytearray(b'\x1e*j           \x1e   NN        g*\x1e'), \
    bytearray(b'\x1e*          jj\x1e          $   *\x1e'), \
    bytearray(b'\x1e*j           \x1e      &\x1e\x1e\x1e\x1e\x1e\x1e\x1e*\x1e'), \
    bytearray(b'\x1e*      $     \x1e    &&  %     *\x1e'), \
    bytearray(b'\x1e\x1e\x1e&&&&&&&&&&&\x1e  && !        *\x1e'), \
    bytearray(b'\x1e       !     \x1e              *\x1e'), \
    bytearray(b'\x1e             \x1eN             *\x1e'), \
    bytearray(b'\x1e             \x1e        gg    *\x1e'), \
    bytearray(b'\x1egg\x1e     NNN\x1e\x1e\x1eggg           g\x1e'), \
    bytearray(b'\x1e  \x1e          \x1e             gg\x1e'), \
    bytearray(b'\x1ej \x1eNNNNNNNN  \x1e            gg%\x1e'), \
    bytearray(b'\x1e                         gg%%\x1e'), \
    bytearray(b'\x1ej                       gg%%%\x1e'), \
    bytearray(b'\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e')])

levels.append([ \
    bytearray(b'YYYYYYYYYYY                 YYY'), \
    bytearray(b'XXXXXXXXXXX   N N NNN       YYY'), \
    bytearray(b'\x1e\x1e_`abc\x1e\x1e\x1e\x1e  N N!N N N      YYY'), \
    bytearray(b'\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e                 XXX'), \
    bytearray(b'e!        e     $       gg  \x1eV\x1e'), \
    bytearray(b'f         d&&&&&    &&&&&   \x1eW\x1e'), \
    bytearray(b'f              &    &       \x1e\x1e\x1e'), \
    bytearray(b'd              &&&&&&       \x1eV\x1e'), \
    bytearray(b'\x1egjjjjggggegg       $       \x1eW\x1e'), \
    bytearray(b'\x1e         f       gg\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e'), \
    bytearray(b'\x1e jjj     f  ggg    \x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e'), \
    bytearray(b'\x1e         f         \x1eVV\x1e\x1eVV\x1eVV\x1e'), \
    bytearray(b'\x1e jjj     f!   ggg  \x1eWW\x1e\x1eWW\x1eWW\x1e'), \
    bytearray(b'\x1e         f          %  \x1e\x1e\x1e\x1e\x1e\x1e\x1e'), \
    bytearray(b'\x1e jjj     f   ggg    !  \x1e\x1e\x1e\x1e\x1e\x1e\x1e'), \
    bytearray(b'\x1e%   N  ! f             \x1eVV\x1eVV\x1e'), \
    bytearray(b'\x1eNNNNNNN\x1e\x1ef  ggg        \x1eWW\x1eWW\x1e'), \
    bytearray(b'\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1ed  N NN N N   \x1e\x1e\x1e\x1e\x1e\x1e\x1e'), \
    bytearray(b'\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e')])

levelSprites.append([ \
    {'position':(396, 52), 'direction':'stand_right'},  \
    {'position':(427, 133)},  \
    {'position': (232, 276), 'nro': 3, 'endpoints': (195, 367), 'direction': 'right'}])

levelSprites.append([ \
    {'position': (40, 36)}, \
    {'position': (457, 274)}, \
    {'position': (136, 84), 'nro': 5, 'endpoints': (40, 328), 'direction': 'right'}, \
    {'position': (40, 276), 'nro': 5, 'endpoints': (40, 296), 'direction': 'right'}])
