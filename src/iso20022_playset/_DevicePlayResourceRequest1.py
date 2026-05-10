from . import base_types
from ._ProcessingPosition2Code import ProcessingPosition2Code
from ._ResourceAction1Code import ResourceAction1Code
from ._ResponseMode2Code import ResponseMode2Code
from ._Max35Text import Max35Text
from ._ResourceContent1 import ResourceContent1
from ._PercentageRate import PercentageRate

class DevicePlayResourceRequest1(base_types._BaseFieldType):

	__slots__ = ["_TmgSlot", "_SoundVol", "_RspnMd", "_Rsrc", "_RsrcActn", "_DispRsltn"]
	@property
	def TmgSlot(self):
		return self._TmgSlot

	@TmgSlot.setter
	def TmgSlot(self, value):
		self._TmgSlot = value if type(value) != base_types.auto else self.make_default("TmgSlot")

	@TmgSlot.deleter
	def TmgSlot(self):
		del self._TmgSlot
		self._TmgSlot = None

	@property
	def SoundVol(self):
		return self._SoundVol

	@SoundVol.setter
	def SoundVol(self, value):
		self._SoundVol = value if type(value) != base_types.auto else self.make_default("SoundVol")

	@SoundVol.deleter
	def SoundVol(self):
		del self._SoundVol
		self._SoundVol = None

	@property
	def RspnMd(self):
		return self._RspnMd

	@RspnMd.setter
	def RspnMd(self, value):
		self._RspnMd = value if type(value) != base_types.auto else self.make_default("RspnMd")

	@RspnMd.deleter
	def RspnMd(self):
		del self._RspnMd
		self._RspnMd = None

	@property
	def Rsrc(self):
		return self._Rsrc

	@Rsrc.setter
	def Rsrc(self, value):
		self._Rsrc = value if type(value) != base_types.auto else self.make_default("Rsrc")

	@Rsrc.deleter
	def Rsrc(self):
		del self._Rsrc
		self._Rsrc = None

	@property
	def RsrcActn(self):
		return self._RsrcActn

	@RsrcActn.setter
	def RsrcActn(self, value):
		self._RsrcActn = value if type(value) != base_types.auto else self.make_default("RsrcActn")

	@RsrcActn.deleter
	def RsrcActn(self):
		del self._RsrcActn
		self._RsrcActn = None

	@property
	def DispRsltn(self):
		return self._DispRsltn

	@DispRsltn.setter
	def DispRsltn(self, value):
		self._DispRsltn = value if type(value) != base_types.auto else self.make_default("DispRsltn")

	@DispRsltn.deleter
	def DispRsltn(self):
		del self._DispRsltn
		self._DispRsltn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TmgSlot', type=ProcessingPosition2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SoundVol', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnMd', type=ResponseMode2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsrc', type=ResourceContent1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsrcActn', type=ResourceAction1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DispRsltn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

