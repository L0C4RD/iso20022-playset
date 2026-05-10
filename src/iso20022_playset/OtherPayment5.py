import base_types
import AmountAndDirection106
import ISODate
import PaymentType5Choice
import PartyIdentification236Choice

class OtherPayment5(base_types._BaseFieldType):

	__slots__ = ["_PmtDt", "_PmtAmt", "_PmtPyer", "_PmtRcvr", "_PmtTp"]
	@property
	def PmtDt(self):
		return self._PmtDt

	@PmtDt.setter
	def PmtDt(self, value):
		self._PmtDt = value if type(value) != auto else self.make_default("PmtDt")

	@PmtDt.deleter
	def PmtDt(self):
		del self._PmtDt
		self._PmtDt = None

	@property
	def PmtAmt(self):
		return self._PmtAmt

	@PmtAmt.setter
	def PmtAmt(self, value):
		self._PmtAmt = value if type(value) != auto else self.make_default("PmtAmt")

	@PmtAmt.deleter
	def PmtAmt(self):
		del self._PmtAmt
		self._PmtAmt = None

	@property
	def PmtPyer(self):
		return self._PmtPyer

	@PmtPyer.setter
	def PmtPyer(self, value):
		self._PmtPyer = value if type(value) != auto else self.make_default("PmtPyer")

	@PmtPyer.deleter
	def PmtPyer(self):
		del self._PmtPyer
		self._PmtPyer = None

	@property
	def PmtRcvr(self):
		return self._PmtRcvr

	@PmtRcvr.setter
	def PmtRcvr(self, value):
		self._PmtRcvr = value if type(value) != auto else self.make_default("PmtRcvr")

	@PmtRcvr.deleter
	def PmtRcvr(self):
		del self._PmtRcvr
		self._PmtRcvr = None

	@property
	def PmtTp(self):
		return self._PmtTp

	@PmtTp.setter
	def PmtTp(self, value):
		self._PmtTp = value if type(value) != auto else self.make_default("PmtTp")

	@PmtTp.deleter
	def PmtTp(self):
		del self._PmtTp
		self._PmtTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PmtDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtAmt', type=AmountAndDirection106, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtPyer', type=PartyIdentification236Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtRcvr', type=PartyIdentification236Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtTp', type=PaymentType5Choice, min=0, max=1, mutex_group=None, array=False),
	))

