import base_types
import TrueFalseIndicator
import CardDataReading8Code
import ActionMessage11
import Number

class DeviceInitialisationCardReaderRequest6(base_types._BaseFieldType):

	__slots__ = ["_DispOutpt", "_WarmRstFlg", "_LeavCardFlg", "_MaxWtgTm", "_ForceNtryMd"]
	@property
	def DispOutpt(self):
		return self._DispOutpt

	@DispOutpt.setter
	def DispOutpt(self, value):
		self._DispOutpt = value if type(value) != auto else self.make_default("DispOutpt")

	@DispOutpt.deleter
	def DispOutpt(self):
		del self._DispOutpt
		self._DispOutpt = None

	@property
	def WarmRstFlg(self):
		return self._WarmRstFlg

	@WarmRstFlg.setter
	def WarmRstFlg(self, value):
		self._WarmRstFlg = value if type(value) != auto else self.make_default("WarmRstFlg")

	@WarmRstFlg.deleter
	def WarmRstFlg(self):
		del self._WarmRstFlg
		self._WarmRstFlg = None

	@property
	def LeavCardFlg(self):
		return self._LeavCardFlg

	@LeavCardFlg.setter
	def LeavCardFlg(self, value):
		self._LeavCardFlg = value if type(value) != auto else self.make_default("LeavCardFlg")

	@LeavCardFlg.deleter
	def LeavCardFlg(self):
		del self._LeavCardFlg
		self._LeavCardFlg = None

	@property
	def MaxWtgTm(self):
		return self._MaxWtgTm

	@MaxWtgTm.setter
	def MaxWtgTm(self, value):
		self._MaxWtgTm = value if type(value) != auto else self.make_default("MaxWtgTm")

	@MaxWtgTm.deleter
	def MaxWtgTm(self):
		del self._MaxWtgTm
		self._MaxWtgTm = None

	@property
	def ForceNtryMd(self):
		return self._ForceNtryMd

	@ForceNtryMd.setter
	def ForceNtryMd(self, value):
		self._ForceNtryMd = value if type(value) != auto else self.make_default("ForceNtryMd")

	@ForceNtryMd.deleter
	def ForceNtryMd(self):
		del self._ForceNtryMd
		self._ForceNtryMd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DispOutpt', type=ActionMessage11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WarmRstFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LeavCardFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxWtgTm', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ForceNtryMd', type=CardDataReading8Code, min=0, max=None, mutex_group=None, array=True),
	))

