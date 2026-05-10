from . import base_types
from .AmountOrRate1Choice import AmountOrRate1Choice
from .TrueFalseIndicator import TrueFalseIndicator
from .Max140Text import Max140Text

class PaymentCondition2(base_types._BaseFieldType):

	__slots__ = ["_GrntedPmtReqd", "_DelyPnlty", "_ImdtPmtRbt", "_EarlyPmtAllwd", "_AmtModAllwd"]
	@property
	def GrntedPmtReqd(self):
		return self._GrntedPmtReqd

	@GrntedPmtReqd.setter
	def GrntedPmtReqd(self, value):
		self._GrntedPmtReqd = value if type(value) != base_types.auto else self.make_default("GrntedPmtReqd")

	@GrntedPmtReqd.deleter
	def GrntedPmtReqd(self):
		del self._GrntedPmtReqd
		self._GrntedPmtReqd = None

	@property
	def DelyPnlty(self):
		return self._DelyPnlty

	@DelyPnlty.setter
	def DelyPnlty(self, value):
		self._DelyPnlty = value if type(value) != base_types.auto else self.make_default("DelyPnlty")

	@DelyPnlty.deleter
	def DelyPnlty(self):
		del self._DelyPnlty
		self._DelyPnlty = None

	@property
	def ImdtPmtRbt(self):
		return self._ImdtPmtRbt

	@ImdtPmtRbt.setter
	def ImdtPmtRbt(self, value):
		self._ImdtPmtRbt = value if type(value) != base_types.auto else self.make_default("ImdtPmtRbt")

	@ImdtPmtRbt.deleter
	def ImdtPmtRbt(self):
		del self._ImdtPmtRbt
		self._ImdtPmtRbt = None

	@property
	def EarlyPmtAllwd(self):
		return self._EarlyPmtAllwd

	@EarlyPmtAllwd.setter
	def EarlyPmtAllwd(self, value):
		self._EarlyPmtAllwd = value if type(value) != base_types.auto else self.make_default("EarlyPmtAllwd")

	@EarlyPmtAllwd.deleter
	def EarlyPmtAllwd(self):
		del self._EarlyPmtAllwd
		self._EarlyPmtAllwd = None

	@property
	def AmtModAllwd(self):
		return self._AmtModAllwd

	@AmtModAllwd.setter
	def AmtModAllwd(self, value):
		self._AmtModAllwd = value if type(value) != base_types.auto else self.make_default("AmtModAllwd")

	@AmtModAllwd.deleter
	def AmtModAllwd(self):
		del self._AmtModAllwd
		self._AmtModAllwd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='GrntedPmtReqd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DelyPnlty', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ImdtPmtRbt', type=AmountOrRate1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EarlyPmtAllwd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmtModAllwd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))

