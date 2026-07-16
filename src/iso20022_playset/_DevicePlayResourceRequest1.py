# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import PercentageRate
from . import ProcessingPosition2Code
from . import ResourceAction1Code
from . import ResourceContent1
from . import ResponseMode2Code

class DevicePlayResourceRequest1(base_types._BaseFieldType):

	__slots__ = ["_DispRsltn", "_RspnMd", "_Rsrc", "_RsrcActn", "_SoundVol", "_TmgSlot"]
	@property
	def DispRsltn(self):
		return self._DispRsltn

	@DispRsltn.setter
	def DispRsltn(self, value):
		self._DispRsltn = value if value is not None else base_types.UninitialisedField(self, 'DispRsltn', Max35Text, False)

	@DispRsltn.deleter
	def DispRsltn(self):
		del self._DispRsltn
		self._DispRsltn = base_types.UninitialisedField(self, 'DispRsltn', Max35Text, False)

	@property
	def RspnMd(self):
		return self._RspnMd

	@RspnMd.setter
	def RspnMd(self, value):
		self._RspnMd = value if value is not None else base_types.UninitialisedField(self, 'RspnMd', ResponseMode2Code, False)

	@RspnMd.deleter
	def RspnMd(self):
		del self._RspnMd
		self._RspnMd = base_types.UninitialisedField(self, 'RspnMd', ResponseMode2Code, False)

	@property
	def Rsrc(self):
		return self._Rsrc

	@Rsrc.setter
	def Rsrc(self, value):
		self._Rsrc = value if value is not None else base_types.UninitialisedField(self, 'Rsrc', ResourceContent1, False)

	@Rsrc.deleter
	def Rsrc(self):
		del self._Rsrc
		self._Rsrc = base_types.UninitialisedField(self, 'Rsrc', ResourceContent1, False)

	@property
	def RsrcActn(self):
		return self._RsrcActn

	@RsrcActn.setter
	def RsrcActn(self, value):
		self._RsrcActn = value if value is not None else base_types.UninitialisedField(self, 'RsrcActn', ResourceAction1Code, False)

	@RsrcActn.deleter
	def RsrcActn(self):
		del self._RsrcActn
		self._RsrcActn = base_types.UninitialisedField(self, 'RsrcActn', ResourceAction1Code, False)

	@property
	def SoundVol(self):
		return self._SoundVol

	@SoundVol.setter
	def SoundVol(self, value):
		self._SoundVol = value if value is not None else base_types.UninitialisedField(self, 'SoundVol', PercentageRate, False)

	@SoundVol.deleter
	def SoundVol(self):
		del self._SoundVol
		self._SoundVol = base_types.UninitialisedField(self, 'SoundVol', PercentageRate, False)

	@property
	def TmgSlot(self):
		return self._TmgSlot

	@TmgSlot.setter
	def TmgSlot(self, value):
		self._TmgSlot = value if value is not None else base_types.UninitialisedField(self, 'TmgSlot', ProcessingPosition2Code, False)

	@TmgSlot.deleter
	def TmgSlot(self):
		del self._TmgSlot
		self._TmgSlot = base_types.UninitialisedField(self, 'TmgSlot', ProcessingPosition2Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DispRsltn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnMd', type=ResponseMode2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsrc', type=ResourceContent1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsrcActn', type=ResourceAction1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SoundVol', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TmgSlot', type=ProcessingPosition2Code, min=0, max=1, mutex_group=None, array=False),
	))