# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import ISODateTime
from . import Max256Text
from . import Max350Text
from . import Max35Text
from . import YesNoIndicator

class TransferInstruction1(base_types._BaseFieldType):

	__slots__ = ["_Cd", "_Desc", "_Prtry", "_StartDt", "_StartDtTm", "_TrfInd"]
	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if value is not None else base_types.UninitialisedField(self, 'Cd', Max35Text, False)

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = base_types.UninitialisedField(self, 'Cd', Max35Text, False)

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if value is not None else base_types.UninitialisedField(self, 'Desc', Max350Text, False)

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = base_types.UninitialisedField(self, 'Desc', Max350Text, False)

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if value is not None else base_types.UninitialisedField(self, 'Prtry', Max256Text, False)

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = base_types.UninitialisedField(self, 'Prtry', Max256Text, False)

	@property
	def StartDt(self):
		return self._StartDt

	@StartDt.setter
	def StartDt(self, value):
		self._StartDt = value if value is not None else base_types.UninitialisedField(self, 'StartDt', ISODate, False)

	@StartDt.deleter
	def StartDt(self):
		del self._StartDt
		self._StartDt = base_types.UninitialisedField(self, 'StartDt', ISODate, False)

	@property
	def StartDtTm(self):
		return self._StartDtTm

	@StartDtTm.setter
	def StartDtTm(self, value):
		self._StartDtTm = value if value is not None else base_types.UninitialisedField(self, 'StartDtTm', ISODateTime, False)

	@StartDtTm.deleter
	def StartDtTm(self):
		del self._StartDtTm
		self._StartDtTm = base_types.UninitialisedField(self, 'StartDtTm', ISODateTime, False)

	@property
	def TrfInd(self):
		return self._TrfInd

	@TrfInd.setter
	def TrfInd(self, value):
		self._TrfInd = value if value is not None else base_types.UninitialisedField(self, 'TrfInd', YesNoIndicator, False)

	@TrfInd.deleter
	def TrfInd(self):
		del self._TrfInd
		self._TrfInd = base_types.UninitialisedField(self, 'TrfInd', YesNoIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cd', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prtry', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))