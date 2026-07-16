# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection106
from . import ISODate
from . import PartyIdentification236Choice
from . import PaymentType5Choice

class OtherPayment5(base_types._BaseFieldType):

	__slots__ = ["_PmtAmt", "_PmtDt", "_PmtPyer", "_PmtRcvr", "_PmtTp"]
	@property
	def PmtAmt(self):
		return self._PmtAmt

	@PmtAmt.setter
	def PmtAmt(self, value):
		self._PmtAmt = value if value is not None else base_types.UninitialisedField(self, 'PmtAmt', AmountAndDirection106, False)

	@PmtAmt.deleter
	def PmtAmt(self):
		del self._PmtAmt
		self._PmtAmt = base_types.UninitialisedField(self, 'PmtAmt', AmountAndDirection106, False)

	@property
	def PmtDt(self):
		return self._PmtDt

	@PmtDt.setter
	def PmtDt(self, value):
		self._PmtDt = value if value is not None else base_types.UninitialisedField(self, 'PmtDt', ISODate, False)

	@PmtDt.deleter
	def PmtDt(self):
		del self._PmtDt
		self._PmtDt = base_types.UninitialisedField(self, 'PmtDt', ISODate, False)

	@property
	def PmtPyer(self):
		return self._PmtPyer

	@PmtPyer.setter
	def PmtPyer(self, value):
		self._PmtPyer = value if value is not None else base_types.UninitialisedField(self, 'PmtPyer', PartyIdentification236Choice, False)

	@PmtPyer.deleter
	def PmtPyer(self):
		del self._PmtPyer
		self._PmtPyer = base_types.UninitialisedField(self, 'PmtPyer', PartyIdentification236Choice, False)

	@property
	def PmtRcvr(self):
		return self._PmtRcvr

	@PmtRcvr.setter
	def PmtRcvr(self, value):
		self._PmtRcvr = value if value is not None else base_types.UninitialisedField(self, 'PmtRcvr', PartyIdentification236Choice, False)

	@PmtRcvr.deleter
	def PmtRcvr(self):
		del self._PmtRcvr
		self._PmtRcvr = base_types.UninitialisedField(self, 'PmtRcvr', PartyIdentification236Choice, False)

	@property
	def PmtTp(self):
		return self._PmtTp

	@PmtTp.setter
	def PmtTp(self, value):
		self._PmtTp = value if value is not None else base_types.UninitialisedField(self, 'PmtTp', PaymentType5Choice, False)

	@PmtTp.deleter
	def PmtTp(self):
		del self._PmtTp
		self._PmtTp = base_types.UninitialisedField(self, 'PmtTp', PaymentType5Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PmtAmt', type=AmountAndDirection106, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtPyer', type=PartyIdentification236Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtRcvr', type=PartyIdentification236Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtTp', type=PaymentType5Choice, min=0, max=1, mutex_group=None, array=False),
	))