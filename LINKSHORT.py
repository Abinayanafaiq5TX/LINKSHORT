U
    $I�^Y  �                   @   s�   d dl Z d dlZd dlZd dlZd dlZd dlmZ dZdZdZdZ	dZ
dZd	Zd
ZdZdZdZdZdZdZdZdZdZdZdZdZdZdZdZd
ZdZdZdZ d	Z!dZ"dZ#dZ$e�%d� e�&�  dd� Zdd� Z'dd� Z(dd � Z)e)�  dS )!�    N)�logoz[32;1mz[0;32mz[34;1mz[36;1mz[31;1mz[0mz[37;1mz[35;1mz[3;1mz[33;1mz[0;33mz[30;1mz[31mz[1;32mz[33mz[34mz[35mz[36mz[37mz[0;36mz[1;33m�clearc                 C   s2   | d D ]$}t j�|� t j��  t�d� qd S )N�
gl�l��?)�sys�stdout�write�flush�time�sleep)�s�c� r   �/sdcard/LINKWHATSAPP.py�kt3   s    
r   c                  C   s�   t t� dt� dt� dt� d��} | �ddd�}ttt t� dt� dt� dt� d����}|�d	d
�}d�||�}tj	dd�}|j
�|�}tt� d�d � tt� dt� dt� dt� d�� d S )N�[�   •�].zMASUKAN NOMOR: �0Z62�   zMASUKAN PESAN :� z%20zhttps://wa.me/{}?text={}�https://0x0.st�Zdomain�=�2   z
LINKSHORT:)�input�sd�kuli�sma�replace�strr   �format�pyshorteners�	Shortener�nullpointer�short�print�mens�a�W)ZnoZga�textZpsn�linkZserverZhar   r   r   �wa9   s     (r+   c                  C   s�   t tt� dt� dt� dt� d���} tjdd�}|j�| �}t	t
� d�d � t	t� dt� dt� d	t� | � t� d
t
� |� �� d S )Nr   r   r   zURL TO SHORT:r   r   r   r   �]. z=>)r   r   r'   r   �aqur!   r"   r#   r$   r   r&   �p�gt)ZabiZdo�binr   r   r   r*   F   s
    $r*   c               	   C   s�   t t� dt� dt� dt� d�� t t� dt� dt� dt� d�� tt� dt� dt� dt� d��} | dkrpt�  n| dkr~t�  d S )	Nr   �1r,   zSHORT WA�2z
SHORT LINKr   zPILIH:)	r   �mr   r&   r   r   �kr+   r*   )Zabinkunr   r   r   �menuL   s       r5   )*r!   r	   r   �osZabinkunsr   �gr/   Zbt�br3   r   r.   �uZzesr4   r   r'   r-   r&   Zmenr   r   Zsmpr   �z�GZGL�B�PZBLZBD�Rr(   �H�YZYL�systemZbannerr+   r*   r5   r   r   r   r   �<module>   sP    
