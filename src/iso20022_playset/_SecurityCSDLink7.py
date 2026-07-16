# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndDateTime2Choice
from . import IssuanceAccount2
from . import SystemPartyIdentification2Choice
from . import YesNoIndicator

class SecurityCSDLink7(base_types._BaseFieldType):

	__slots__ = ["_InvstrCSD", "_IssncAcct", "_IssrCSD", "_SctyMntnc", "_TechIssrCSD", "_VldFr", "_VldTo"]
	@property
	def InvstrCSD(self):
		return self._InvstrCSD

	@InvstrCSD.setter
	def InvstrCSD(self, value):
		self._InvstrCSD = value if value is not None else base_types.UninitialisedField(self, 'InvstrCSD', SystemPartyIdentification2Choice, False)

	@InvstrCSD.deleter
	def InvstrCSD(self):
		del self._InvstrCSD
		self._InvstrCSD = base_types.UninitialisedField(self, 'InvstrCSD', SystemPartyIdentification2Choice, False)

	@property
	def IssncAcct(self):
		return self._IssncAcct

	@IssncAcct.setter
	def IssncAcct(self, value):
		self._IssncAcct = value if value is not None else base_types.UninitialisedField(self, 'IssncAcct', IssuanceAccount2, True)

	@IssncAcct.deleter
	def IssncAcct(self):
		del self._IssncAcct
		self._IssncAcct = base_types.UninitialisedField(self, 'IssncAcct', IssuanceAccount2, True)

	@property
	def IssrCSD(self):
		return self._IssrCSD

	@IssrCSD.setter
	def IssrCSD(self, value):
		self._IssrCSD = value if value is not None else base_types.UninitialisedField(self, 'IssrCSD', SystemPartyIdentification2Choice, False)

	@IssrCSD.deleter
	def IssrCSD(self):
		del self._IssrCSD
		self._IssrCSD = base_types.UninitialisedField(self, 'IssrCSD', SystemPartyIdentification2Choice, False)

	@property
	def SctyMntnc(self):
		return self._SctyMntnc

	@SctyMntnc.setter
	def SctyMntnc(self, value):
		self._SctyMntnc = value if value is not None else base_types.UninitialisedField(self, 'SctyMntnc', YesNoIndicator, False)

	@SctyMntnc.deleter
	def SctyMntnc(self):
		del self._SctyMntnc
		self._SctyMntnc = base_types.UninitialisedField(self, 'SctyMntnc', YesNoIndicator, False)

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
		base_types.FieldEntry(name='InvstrCSD', type=SystemPartyIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssncAcct', type=IssuanceAccount2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IssrCSD', type=SystemPartyIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyMntnc', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechIssrCSD', type=SystemPartyIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldFr', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldTo', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
	))