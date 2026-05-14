# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DateAndDateTime2Choice import DateAndDateTime2Choice
from ._IssuanceAccount3 import IssuanceAccount3
from ._IssuerOrInvestor2Choice import IssuerOrInvestor2Choice
from ._SecurityIdentification19 import SecurityIdentification19
from ._SystemPartyIdentification2Choice import SystemPartyIdentification2Choice
from ._TrueFalseIndicator import TrueFalseIndicator

class SecurityCSDLink12(base_types._BaseFieldType):

	__slots__ = ["_DfltLk", "_FinInstrmId", "_IssncAcct", "_IssrInvstrCSD", "_SctyMntnc", "_TechIssrCSD", "_VldFr", "_VldTo"]
	@property
	def DfltLk(self):
		return self._DfltLk

	@DfltLk.setter
	def DfltLk(self, value):
		self._DfltLk = value if type(value) != base_types.auto else self.make_default("DfltLk")

	@DfltLk.deleter
	def DfltLk(self):
		del self._DfltLk
		self._DfltLk = None

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != base_types.auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	@property
	def IssncAcct(self):
		return self._IssncAcct

	@IssncAcct.setter
	def IssncAcct(self, value):
		self._IssncAcct = value if type(value) != base_types.auto else self.make_default("IssncAcct")

	@IssncAcct.deleter
	def IssncAcct(self):
		del self._IssncAcct
		self._IssncAcct = None

	@property
	def IssrInvstrCSD(self):
		return self._IssrInvstrCSD

	@IssrInvstrCSD.setter
	def IssrInvstrCSD(self, value):
		self._IssrInvstrCSD = value if type(value) != base_types.auto else self.make_default("IssrInvstrCSD")

	@IssrInvstrCSD.deleter
	def IssrInvstrCSD(self):
		del self._IssrInvstrCSD
		self._IssrInvstrCSD = None

	@property
	def SctyMntnc(self):
		return self._SctyMntnc

	@SctyMntnc.setter
	def SctyMntnc(self, value):
		self._SctyMntnc = value if type(value) != base_types.auto else self.make_default("SctyMntnc")

	@SctyMntnc.deleter
	def SctyMntnc(self):
		del self._SctyMntnc
		self._SctyMntnc = None

	@property
	def TechIssrCSD(self):
		return self._TechIssrCSD

	@TechIssrCSD.setter
	def TechIssrCSD(self, value):
		self._TechIssrCSD = value if type(value) != base_types.auto else self.make_default("TechIssrCSD")

	@TechIssrCSD.deleter
	def TechIssrCSD(self):
		del self._TechIssrCSD
		self._TechIssrCSD = None

	@property
	def VldFr(self):
		return self._VldFr

	@VldFr.setter
	def VldFr(self, value):
		self._VldFr = value if type(value) != base_types.auto else self.make_default("VldFr")

	@VldFr.deleter
	def VldFr(self):
		del self._VldFr
		self._VldFr = None

	@property
	def VldTo(self):
		return self._VldTo

	@VldTo.setter
	def VldTo(self, value):
		self._VldTo = value if type(value) != base_types.auto else self.make_default("VldTo")

	@VldTo.deleter
	def VldTo(self):
		del self._VldTo
		self._VldTo = None

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