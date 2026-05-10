from . import base_types
import EligibilityDates1
import SupplementaryData1
import PartyIdentification129Choice
import Max35Text
import NotificationType2Code
import PartyIdentification232Choice
import MeetingReference10
import SecurityPosition21

class MeetingEntitlementNotificationV10(base_types._BaseFieldType):

	__slots__ = ["_NtfctnTp", "_SplmtryData", "_Issr", "_MtgAttndee", "_MtgRef", "_Prxy", "_Scty", "_Elgblty", "_PrvsEntitlmntNtfctnId"]
	@property
	def NtfctnTp(self):
		return self._NtfctnTp

	@NtfctnTp.setter
	def NtfctnTp(self, value):
		self._NtfctnTp = value if type(value) != auto else self.make_default("NtfctnTp")

	@NtfctnTp.deleter
	def NtfctnTp(self):
		del self._NtfctnTp
		self._NtfctnTp = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if type(value) != auto else self.make_default("Issr")

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = None

	@property
	def MtgAttndee(self):
		return self._MtgAttndee

	@MtgAttndee.setter
	def MtgAttndee(self, value):
		self._MtgAttndee = value if type(value) != auto else self.make_default("MtgAttndee")

	@MtgAttndee.deleter
	def MtgAttndee(self):
		del self._MtgAttndee
		self._MtgAttndee = None

	@property
	def MtgRef(self):
		return self._MtgRef

	@MtgRef.setter
	def MtgRef(self, value):
		self._MtgRef = value if type(value) != auto else self.make_default("MtgRef")

	@MtgRef.deleter
	def MtgRef(self):
		del self._MtgRef
		self._MtgRef = None

	@property
	def Prxy(self):
		return self._Prxy

	@Prxy.setter
	def Prxy(self, value):
		self._Prxy = value if type(value) != auto else self.make_default("Prxy")

	@Prxy.deleter
	def Prxy(self):
		del self._Prxy
		self._Prxy = None

	@property
	def Scty(self):
		return self._Scty

	@Scty.setter
	def Scty(self, value):
		self._Scty = value if type(value) != auto else self.make_default("Scty")

	@Scty.deleter
	def Scty(self):
		del self._Scty
		self._Scty = None

	@property
	def Elgblty(self):
		return self._Elgblty

	@Elgblty.setter
	def Elgblty(self, value):
		self._Elgblty = value if type(value) != auto else self.make_default("Elgblty")

	@Elgblty.deleter
	def Elgblty(self):
		del self._Elgblty
		self._Elgblty = None

	@property
	def PrvsEntitlmntNtfctnId(self):
		return self._PrvsEntitlmntNtfctnId

	@PrvsEntitlmntNtfctnId.setter
	def PrvsEntitlmntNtfctnId(self, value):
		self._PrvsEntitlmntNtfctnId = value if type(value) != auto else self.make_default("PrvsEntitlmntNtfctnId")

	@PrvsEntitlmntNtfctnId.deleter
	def PrvsEntitlmntNtfctnId(self):
		del self._PrvsEntitlmntNtfctnId
		self._PrvsEntitlmntNtfctnId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NtfctnTp', type=NotificationType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Issr', type=PartyIdentification129Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtgAttndee', type=PartyIdentification232Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtgRef', type=MeetingReference10, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prxy', type=PartyIdentification232Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Scty', type=SecurityPosition21, min=1, max=200, mutex_group=None, array=True),
		base_types.FieldEntry(name='Elgblty', type=EligibilityDates1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsEntitlmntNtfctnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

