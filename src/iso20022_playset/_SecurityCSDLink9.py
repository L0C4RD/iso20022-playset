# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndDateTime2Choice
from . import IssuerOrInvestor2Choice
from . import SecurityIdentification19

class SecurityCSDLink9(base_types._BaseFieldType):

	__slots__ = ["_FinInstrmId", "_IssrInvstrCSD", "_VldFr"]
	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, False)

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, False)

	@property
	def IssrInvstrCSD(self):
		return self._IssrInvstrCSD

	@IssrInvstrCSD.setter
	def IssrInvstrCSD(self, value):
		self._IssrInvstrCSD = value if value is not None else base_types.UninitialisedField(self, 'IssrInvstrCSD', IssuerOrInvestor2Choice, False)

	@IssrInvstrCSD.deleter
	def IssrInvstrCSD(self):
		del self._IssrInvstrCSD
		self._IssrInvstrCSD = base_types.UninitialisedField(self, 'IssrInvstrCSD', IssuerOrInvestor2Choice, False)

	@property
	def VldFr(self):
		return self._VldFr

	@VldFr.setter
	def VldFr(self, value):
		self._VldFr = value if value is not None else base_types.UninitialisedField(self, 'VldFr', DateAndDateTime2Choice, False)

	@VldFr.deleter
	def VldFr(self):
		del self._VldFr
		self._VldFr = base_types.UninitialisedField(self, 'VldFr', DateAndDateTime2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrInvstrCSD', type=IssuerOrInvestor2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldFr', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
	))