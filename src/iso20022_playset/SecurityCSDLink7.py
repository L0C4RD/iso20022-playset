import base_types
import SystemPartyIdentification2Choice
import IssuanceAccount2
import YesNoIndicator
import DateAndDateTime2Choice

class SecurityCSDLink7(base_types._BaseFieldType):

	__slots__ = ["_VldTo", "_SctyMntnc", "_VldFr", "_IssrCSD", "_IssncAcct", "_InvstrCSD", "_TechIssrCSD"]
	@property
	def VldTo(self):
		return self._VldTo

	@VldTo.setter
	def VldTo(self, value):
		self._VldTo = value if type(value) != auto else self.make_default("VldTo")

	@VldTo.deleter
	def VldTo(self):
		del self._VldTo
		self._VldTo = None

	@property
	def SctyMntnc(self):
		return self._SctyMntnc

	@SctyMntnc.setter
	def SctyMntnc(self, value):
		self._SctyMntnc = value if type(value) != auto else self.make_default("SctyMntnc")

	@SctyMntnc.deleter
	def SctyMntnc(self):
		del self._SctyMntnc
		self._SctyMntnc = None

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
	def IssrCSD(self):
		return self._IssrCSD

	@IssrCSD.setter
	def IssrCSD(self, value):
		self._IssrCSD = value if type(value) != auto else self.make_default("IssrCSD")

	@IssrCSD.deleter
	def IssrCSD(self):
		del self._IssrCSD
		self._IssrCSD = None

	@property
	def IssncAcct(self):
		return self._IssncAcct

	@IssncAcct.setter
	def IssncAcct(self, value):
		self._IssncAcct = value if type(value) != auto else self.make_default("IssncAcct")

	@IssncAcct.deleter
	def IssncAcct(self):
		del self._IssncAcct
		self._IssncAcct = None

	@property
	def InvstrCSD(self):
		return self._InvstrCSD

	@InvstrCSD.setter
	def InvstrCSD(self, value):
		self._InvstrCSD = value if type(value) != auto else self.make_default("InvstrCSD")

	@InvstrCSD.deleter
	def InvstrCSD(self):
		del self._InvstrCSD
		self._InvstrCSD = None

	@property
	def TechIssrCSD(self):
		return self._TechIssrCSD

	@TechIssrCSD.setter
	def TechIssrCSD(self, value):
		self._TechIssrCSD = value if type(value) != auto else self.make_default("TechIssrCSD")

	@TechIssrCSD.deleter
	def TechIssrCSD(self):
		del self._TechIssrCSD
		self._TechIssrCSD = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='VldTo', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyMntnc', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldFr', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrCSD', type=SystemPartyIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssncAcct', type=IssuanceAccount2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InvstrCSD', type=SystemPartyIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechIssrCSD', type=SystemPartyIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
	))

