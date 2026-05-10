import base_types
import SecurityIdentification19
import IssuerOrInvestor2Choice
import DateAndDateTime2Choice

class SecurityCSDLink9(base_types._BaseFieldType):

	__slots__ = ["_VldFr", "_IssrInvstrCSD", "_FinInstrmId"]
	@property
	def VldFr(self):
		return self._VldFr

	@VldFr.setter
	def VldFr(self, value):
		self._VldFr = value if type(value) != auto else self.make_default("VldFr")

	@VldFr.deleter
	def VldFr(self):
		del self._VldFr
		self._VldFr = None

	@property
	def IssrInvstrCSD(self):
		return self._IssrInvstrCSD

	@IssrInvstrCSD.setter
	def IssrInvstrCSD(self, value):
		self._IssrInvstrCSD = value if type(value) != auto else self.make_default("IssrInvstrCSD")

	@IssrInvstrCSD.deleter
	def IssrInvstrCSD(self):
		del self._IssrInvstrCSD
		self._IssrInvstrCSD = None

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='VldFr', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrInvstrCSD', type=IssuerOrInvestor2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
	))

