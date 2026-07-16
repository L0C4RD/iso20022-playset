# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActionMessage11
from . import CardDataReading8Code
from . import Number
from . import TrueFalseIndicator

class DeviceInitialisationCardReaderRequest6(base_types._BaseFieldType):

	__slots__ = ["_DispOutpt", "_ForceNtryMd", "_LeavCardFlg", "_MaxWtgTm", "_WarmRstFlg"]
	@property
	def DispOutpt(self):
		return self._DispOutpt

	@DispOutpt.setter
	def DispOutpt(self, value):
		self._DispOutpt = value if value is not None else base_types.UninitialisedField(self, 'DispOutpt', ActionMessage11, False)

	@DispOutpt.deleter
	def DispOutpt(self):
		del self._DispOutpt
		self._DispOutpt = base_types.UninitialisedField(self, 'DispOutpt', ActionMessage11, False)

	@property
	def ForceNtryMd(self):
		return self._ForceNtryMd

	@ForceNtryMd.setter
	def ForceNtryMd(self, value):
		self._ForceNtryMd = value if value is not None else base_types.UninitialisedField(self, 'ForceNtryMd', CardDataReading8Code, True)

	@ForceNtryMd.deleter
	def ForceNtryMd(self):
		del self._ForceNtryMd
		self._ForceNtryMd = base_types.UninitialisedField(self, 'ForceNtryMd', CardDataReading8Code, True)

	@property
	def LeavCardFlg(self):
		return self._LeavCardFlg

	@LeavCardFlg.setter
	def LeavCardFlg(self, value):
		self._LeavCardFlg = value if value is not None else base_types.UninitialisedField(self, 'LeavCardFlg', TrueFalseIndicator, False)

	@LeavCardFlg.deleter
	def LeavCardFlg(self):
		del self._LeavCardFlg
		self._LeavCardFlg = base_types.UninitialisedField(self, 'LeavCardFlg', TrueFalseIndicator, False)

	@property
	def MaxWtgTm(self):
		return self._MaxWtgTm

	@MaxWtgTm.setter
	def MaxWtgTm(self, value):
		self._MaxWtgTm = value if value is not None else base_types.UninitialisedField(self, 'MaxWtgTm', Number, False)

	@MaxWtgTm.deleter
	def MaxWtgTm(self):
		del self._MaxWtgTm
		self._MaxWtgTm = base_types.UninitialisedField(self, 'MaxWtgTm', Number, False)

	@property
	def WarmRstFlg(self):
		return self._WarmRstFlg

	@WarmRstFlg.setter
	def WarmRstFlg(self, value):
		self._WarmRstFlg = value if value is not None else base_types.UninitialisedField(self, 'WarmRstFlg', TrueFalseIndicator, False)

	@WarmRstFlg.deleter
	def WarmRstFlg(self):
		del self._WarmRstFlg
		self._WarmRstFlg = base_types.UninitialisedField(self, 'WarmRstFlg', TrueFalseIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DispOutpt', type=ActionMessage11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ForceNtryMd', type=CardDataReading8Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LeavCardFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxWtgTm', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WarmRstFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))