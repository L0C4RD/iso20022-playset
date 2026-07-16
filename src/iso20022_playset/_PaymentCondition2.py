# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountOrRate1Choice
from . import Max140Text
from . import TrueFalseIndicator

class PaymentCondition2(base_types._BaseFieldType):

	__slots__ = ["_AmtModAllwd", "_DelyPnlty", "_EarlyPmtAllwd", "_GrntedPmtReqd", "_ImdtPmtRbt"]
	@property
	def AmtModAllwd(self):
		return self._AmtModAllwd

	@AmtModAllwd.setter
	def AmtModAllwd(self, value):
		self._AmtModAllwd = value if value is not None else base_types.UninitialisedField(self, 'AmtModAllwd', TrueFalseIndicator, False)

	@AmtModAllwd.deleter
	def AmtModAllwd(self):
		del self._AmtModAllwd
		self._AmtModAllwd = base_types.UninitialisedField(self, 'AmtModAllwd', TrueFalseIndicator, False)

	@property
	def DelyPnlty(self):
		return self._DelyPnlty

	@DelyPnlty.setter
	def DelyPnlty(self, value):
		self._DelyPnlty = value if value is not None else base_types.UninitialisedField(self, 'DelyPnlty', Max140Text, False)

	@DelyPnlty.deleter
	def DelyPnlty(self):
		del self._DelyPnlty
		self._DelyPnlty = base_types.UninitialisedField(self, 'DelyPnlty', Max140Text, False)

	@property
	def EarlyPmtAllwd(self):
		return self._EarlyPmtAllwd

	@EarlyPmtAllwd.setter
	def EarlyPmtAllwd(self, value):
		self._EarlyPmtAllwd = value if value is not None else base_types.UninitialisedField(self, 'EarlyPmtAllwd', TrueFalseIndicator, False)

	@EarlyPmtAllwd.deleter
	def EarlyPmtAllwd(self):
		del self._EarlyPmtAllwd
		self._EarlyPmtAllwd = base_types.UninitialisedField(self, 'EarlyPmtAllwd', TrueFalseIndicator, False)

	@property
	def GrntedPmtReqd(self):
		return self._GrntedPmtReqd

	@GrntedPmtReqd.setter
	def GrntedPmtReqd(self, value):
		self._GrntedPmtReqd = value if value is not None else base_types.UninitialisedField(self, 'GrntedPmtReqd', TrueFalseIndicator, False)

	@GrntedPmtReqd.deleter
	def GrntedPmtReqd(self):
		del self._GrntedPmtReqd
		self._GrntedPmtReqd = base_types.UninitialisedField(self, 'GrntedPmtReqd', TrueFalseIndicator, False)

	@property
	def ImdtPmtRbt(self):
		return self._ImdtPmtRbt

	@ImdtPmtRbt.setter
	def ImdtPmtRbt(self, value):
		self._ImdtPmtRbt = value if value is not None else base_types.UninitialisedField(self, 'ImdtPmtRbt', AmountOrRate1Choice, False)

	@ImdtPmtRbt.deleter
	def ImdtPmtRbt(self):
		del self._ImdtPmtRbt
		self._ImdtPmtRbt = base_types.UninitialisedField(self, 'ImdtPmtRbt', AmountOrRate1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmtModAllwd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DelyPnlty', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EarlyPmtAllwd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrntedPmtReqd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ImdtPmtRbt', type=AmountOrRate1Choice, min=0, max=1, mutex_group=None, array=False),
	))