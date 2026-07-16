# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionBalance50
from . import EventInformation17
from . import SecurityIdentification19
from . import SupplementaryData1

class CorporateActionEventAndBalance26(base_types._BaseFieldType):

	__slots__ = ["_Bal", "_GnlInf", "_SplmtryData", "_UndrlygScty"]
	@property
	def Bal(self):
		return self._Bal

	@Bal.setter
	def Bal(self, value):
		self._Bal = value if value is not None else base_types.UninitialisedField(self, 'Bal', CorporateActionBalance50, False)

	@Bal.deleter
	def Bal(self):
		del self._Bal
		self._Bal = base_types.UninitialisedField(self, 'Bal', CorporateActionBalance50, False)

	@property
	def GnlInf(self):
		return self._GnlInf

	@GnlInf.setter
	def GnlInf(self, value):
		self._GnlInf = value if value is not None else base_types.UninitialisedField(self, 'GnlInf', EventInformation17, False)

	@GnlInf.deleter
	def GnlInf(self):
		del self._GnlInf
		self._GnlInf = base_types.UninitialisedField(self, 'GnlInf', EventInformation17, False)

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

	@property
	def UndrlygScty(self):
		return self._UndrlygScty

	@UndrlygScty.setter
	def UndrlygScty(self, value):
		self._UndrlygScty = value if value is not None else base_types.UninitialisedField(self, 'UndrlygScty', SecurityIdentification19, False)

	@UndrlygScty.deleter
	def UndrlygScty(self):
		del self._UndrlygScty
		self._UndrlygScty = base_types.UninitialisedField(self, 'UndrlygScty', SecurityIdentification19, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Bal', type=CorporateActionBalance50, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GnlInf', type=EventInformation17, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='UndrlygScty', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
	))