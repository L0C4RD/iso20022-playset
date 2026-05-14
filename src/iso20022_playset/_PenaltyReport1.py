from . import base_types
from ._DateAndDateTime2Choice import DateAndDateTime2Choice
from ._DatePeriod1Choice import DatePeriod1Choice
from ._Frequency22Choice import Frequency22Choice
from ._Max35Text import Max35Text
from ._PenaltyListType1Choice import PenaltyListType1Choice
from ._UpdateType15Choice import UpdateType15Choice
from ._YesNoIndicator import YesNoIndicator

class PenaltyReport1(base_types._BaseFieldType):

	__slots__ = ["_ActvtyInd", "_Frqcy", "_PnltyListTp", "_RptDt", "_RptId", "_RptPrd", "_UpdTp"]
	@property
	def ActvtyInd(self):
		return self._ActvtyInd

	@ActvtyInd.setter
	def ActvtyInd(self, value):
		self._ActvtyInd = value if type(value) != base_types.auto else self.make_default("ActvtyInd")

	@ActvtyInd.deleter
	def ActvtyInd(self):
		del self._ActvtyInd
		self._ActvtyInd = None

	@property
	def Frqcy(self):
		return self._Frqcy

	@Frqcy.setter
	def Frqcy(self, value):
		self._Frqcy = value if type(value) != base_types.auto else self.make_default("Frqcy")

	@Frqcy.deleter
	def Frqcy(self):
		del self._Frqcy
		self._Frqcy = None

	@property
	def PnltyListTp(self):
		return self._PnltyListTp

	@PnltyListTp.setter
	def PnltyListTp(self, value):
		self._PnltyListTp = value if type(value) != base_types.auto else self.make_default("PnltyListTp")

	@PnltyListTp.deleter
	def PnltyListTp(self):
		del self._PnltyListTp
		self._PnltyListTp = None

	@property
	def RptDt(self):
		return self._RptDt

	@RptDt.setter
	def RptDt(self, value):
		self._RptDt = value if type(value) != base_types.auto else self.make_default("RptDt")

	@RptDt.deleter
	def RptDt(self):
		del self._RptDt
		self._RptDt = None

	@property
	def RptId(self):
		return self._RptId

	@RptId.setter
	def RptId(self, value):
		self._RptId = value if type(value) != base_types.auto else self.make_default("RptId")

	@RptId.deleter
	def RptId(self):
		del self._RptId
		self._RptId = None

	@property
	def RptPrd(self):
		return self._RptPrd

	@RptPrd.setter
	def RptPrd(self, value):
		self._RptPrd = value if type(value) != base_types.auto else self.make_default("RptPrd")

	@RptPrd.deleter
	def RptPrd(self):
		del self._RptPrd
		self._RptPrd = None

	@property
	def UpdTp(self):
		return self._UpdTp

	@UpdTp.setter
	def UpdTp(self, value):
		self._UpdTp = value if type(value) != base_types.auto else self.make_default("UpdTp")

	@UpdTp.deleter
	def UpdTp(self):
		del self._UpdTp
		self._UpdTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActvtyInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frqcy', type=Frequency22Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PnltyListTp', type=PenaltyListType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptPrd', type=DatePeriod1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UpdTp', type=UpdateType15Choice, min=0, max=1, mutex_group=None, array=False),
	))

