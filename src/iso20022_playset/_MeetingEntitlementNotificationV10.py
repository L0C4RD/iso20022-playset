# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import EligibilityDates1
from . import Max35Text
from . import MeetingReference10
from . import NotificationType2Code
from . import PartyIdentification129Choice
from . import PartyIdentification232Choice
from . import SecurityPosition21
from . import SupplementaryData1

class MeetingEntitlementNotificationV10(base_types._BaseFieldType):

	__slots__ = ["_Elgblty", "_Issr", "_MtgAttndee", "_MtgRef", "_NtfctnTp", "_PrvsEntitlmntNtfctnId", "_Prxy", "_Scty", "_SplmtryData"]
	@property
	def Elgblty(self):
		return self._Elgblty

	@Elgblty.setter
	def Elgblty(self, value):
		self._Elgblty = value if value is not None else base_types.UninitialisedField(self, 'Elgblty', EligibilityDates1, False)

	@Elgblty.deleter
	def Elgblty(self):
		del self._Elgblty
		self._Elgblty = base_types.UninitialisedField(self, 'Elgblty', EligibilityDates1, False)

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if value is not None else base_types.UninitialisedField(self, 'Issr', PartyIdentification129Choice, False)

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = base_types.UninitialisedField(self, 'Issr', PartyIdentification129Choice, False)

	@property
	def MtgAttndee(self):
		return self._MtgAttndee

	@MtgAttndee.setter
	def MtgAttndee(self, value):
		self._MtgAttndee = value if value is not None else base_types.UninitialisedField(self, 'MtgAttndee', PartyIdentification232Choice, False)

	@MtgAttndee.deleter
	def MtgAttndee(self):
		del self._MtgAttndee
		self._MtgAttndee = base_types.UninitialisedField(self, 'MtgAttndee', PartyIdentification232Choice, False)

	@property
	def MtgRef(self):
		return self._MtgRef

	@MtgRef.setter
	def MtgRef(self, value):
		self._MtgRef = value if value is not None else base_types.UninitialisedField(self, 'MtgRef', MeetingReference10, False)

	@MtgRef.deleter
	def MtgRef(self):
		del self._MtgRef
		self._MtgRef = base_types.UninitialisedField(self, 'MtgRef', MeetingReference10, False)

	@property
	def NtfctnTp(self):
		return self._NtfctnTp

	@NtfctnTp.setter
	def NtfctnTp(self, value):
		self._NtfctnTp = value if value is not None else base_types.UninitialisedField(self, 'NtfctnTp', NotificationType2Code, False)

	@NtfctnTp.deleter
	def NtfctnTp(self):
		del self._NtfctnTp
		self._NtfctnTp = base_types.UninitialisedField(self, 'NtfctnTp', NotificationType2Code, False)

	@property
	def PrvsEntitlmntNtfctnId(self):
		return self._PrvsEntitlmntNtfctnId

	@PrvsEntitlmntNtfctnId.setter
	def PrvsEntitlmntNtfctnId(self, value):
		self._PrvsEntitlmntNtfctnId = value if value is not None else base_types.UninitialisedField(self, 'PrvsEntitlmntNtfctnId', Max35Text, False)

	@PrvsEntitlmntNtfctnId.deleter
	def PrvsEntitlmntNtfctnId(self):
		del self._PrvsEntitlmntNtfctnId
		self._PrvsEntitlmntNtfctnId = base_types.UninitialisedField(self, 'PrvsEntitlmntNtfctnId', Max35Text, False)

	@property
	def Prxy(self):
		return self._Prxy

	@Prxy.setter
	def Prxy(self, value):
		self._Prxy = value if value is not None else base_types.UninitialisedField(self, 'Prxy', PartyIdentification232Choice, False)

	@Prxy.deleter
	def Prxy(self):
		del self._Prxy
		self._Prxy = base_types.UninitialisedField(self, 'Prxy', PartyIdentification232Choice, False)

	@property
	def Scty(self):
		return self._Scty

	@Scty.setter
	def Scty(self, value):
		self._Scty = value if value is not None else base_types.UninitialisedField(self, 'Scty', SecurityPosition21, True)

	@Scty.deleter
	def Scty(self):
		del self._Scty
		self._Scty = base_types.UninitialisedField(self, 'Scty', SecurityPosition21, True)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Elgblty', type=EligibilityDates1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=PartyIdentification129Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtgAttndee', type=PartyIdentification232Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtgRef', type=MeetingReference10, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnTp', type=NotificationType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsEntitlmntNtfctnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prxy', type=PartyIdentification232Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Scty', type=SecurityPosition21, min=1, max=200, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))