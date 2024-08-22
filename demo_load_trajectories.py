import TrkFile
import TrxFile
import movies
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches

## show ufmf of flies with keypoint (APT) and ellipse (FlyTracker) tracking

# APT keypoint tracking
trkfilepath = 'demo_trajectory_data/flies/apt.trk'

# Ctrax/FlyTracker ellipse trajectories
trxfilepath = 'demo_trajectory_data/flies/registered_trx.mat'

# ufmf video
moviepath = 'demo_trajectory_data/flies/movie.ufmf'

# frame to plot
t = 1234

# open video
mov = movies.Movie(moviepath)

# load APT trajectories
apttrk = TrkFile.Trk(trkfilepath)

# load Ctrax/FlyTracker trajectories
trx = TrxFile.Trx(trxfilepath)

# read video frame
im,timestamp = mov.get_frame(t)

# read frame from Ctrax trajectories
# dict with each field is nflies in length
ctrax = trx.getframe(t)

# read frame from APT trajectories
# nkeypoints x 2 x nframes x nflies
kp = apttrk.getframe(t)

nflies = kp.shape[-1]

# plot
fig,ax = plt.subplots(1)
ax.imshow(im,vmin=0,vmax=255,cmap='gray')
h = ax.plot(kp[:,0,0,:],kp[:,1,0,:],'.')
for fly in range(nflies):
    ell = patches.Ellipse(xy=(ctrax['x'][fly],ctrax['y'][fly]),
                          width=ctrax['a'][fly]*4.,height=ctrax['b'][fly]*4.,
                          angle=ctrax['theta'][fly]*180./np.pi,
                          facecolor='none',
                          edgecolor=h[fly].get_color())
    ax.add_patch(ell)

fig.tight_layout()
mov.close()
mov = None


## show mjpg of mice with keypoint (APT) tracking

# APT keypoint tracking
trkfilepath = 'demo_trajectory_data/mice/apt.trk'

# mjpg video
moviepath = 'demo_trajectory_data/mice/movie.mjpg'
movieindexpath = 'demo_trajectory_data/mice/movie.txt'

# frame to plot
t = 1234

# open video
mov = movies.Movie(moviepath)

# load APT trajectories
apttrk = TrkFile.Trk(trkfilepath)

# read video frame
im,timestamp = mov.get_frame(t)

# read frame from APT trajectories
# nkeypoints x 2 x nframes x nmice
kp = apttrk.getframe(t)

nmice = kp.shape[-1]

# plot
fig,ax = plt.subplots(1)
ax.imshow(im,vmin=0,vmax=255,cmap='gray')
h = ax.plot(kp[:,0,0,:],kp[:,1,0,:],'.')

fig.tight_layout()
plt.show()
mov.close()
mov = None
