# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndDateTime2Choice
from . import IssuanceAccount3
from . import IssuerOrInvestor2Choice
from . import SecurityIdentification19
from . import SystemPartyIdentification2Choice
from . import TrueFalseIndicator

class SecurityCSDLink12(base_types._BaseFieldType):

	__slots__ = ["_DfltLk", "_FinInstrmId", "_IssncAcct", "_IssrInvstrCSD", "_SctyMntnc", "_TechIssrCSD", "_VldFr", "_VldTo"]
	@property
	def DfltLk(self):
		return self._DfltLk

	@DfltLk.setter
	def DfltLk(self, value):
		self._DfltLk = value if value is not None else base_types.UninitialisedField(self, 'DfltLk', TrueFalseIndicator, False)

	@DfltLk.deleter
	def DfltLk(self):
		del self._DfltLk
		self._DfltLk = base_types.UninitialisedField(self, 'DfltLk', TrueFalseIndicator, False)

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
	def IssncAcct(self):
		return self._IssncAcct

	@IssncAcct.setter
	def IssncAcct(self, value):
		self._IssncAcct = value if value is not None else base_types.UninitialisedField(self, 'IssncAcct', IssuanceAccount3, True)

	@IssncAcct.deleter
	def IssncAcct(self):
		del self._IssncAcct
		self._IssncAcct = base_types.UninitialisedField(self, 'IssncAcct', IssuanceAccount3, True)

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
	def SctyMntnc(self):
		return self._SctyMntnc

	@SctyMntnc.setter
	def SctyMntnc(self, value):
		self._SctyMntnc = value if value is not None else base_types.UninitialisedField(self, 'SctyMntnc', TrueFalseIndicator, False)

	@SctyMntnc.deleter
	def SctyMntnc(self):
		del self._SctyMntnc
		self._SctyMntnc = base_types.UninitialisedField(self, 'SctyMntnc', TrueFalseIndicator, False)

	@property
	def TechIssrCSD(self):
		return self._TechIssrCSD

	@TechIssrCSD.setter
	def TechIssrCSD(self, value):
		self._TechIssrCSD = value if value is not None else base_types.UninitialisedField(self, 'TechIssrCSD', SystemPartyIdentification2Choice, False)

	@TechIssrCSD.deleter
	def TechIssrCSD(self):
		del self._TechIssrCSD
		self._TechIssrCSD = base_types.UninitialisedField(self, 'TechIssrCSD', SystemPartyIdentification2Choice, False)

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

	@property
	def VldTo(self):
		return self._VldTo

	@VldTo.setter
	def VldTo(self, value):
		self._VldTo = value if value is not None else base_types.UninitialisedField(self, 'VldTo', DateAndDateTime2Choice, False)

	@VldTo.deleter
	def VldTo(self):
		del self._VldTo
		self._VldTo = base_types.UninitialisedField(self, 'VldTo', DateAndDateTime2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DfltLk', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssncAcct', type=IssuanceAccount3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IssrInvstrCSD', type=IssuerOrInvestor2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyMntnc', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechIssrCSD', type=SystemPartyIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldFr', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldTo', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
	))