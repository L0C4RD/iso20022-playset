# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateTimePeriod2
from . import Max350Text
from . import Max35Text
from . import PartyIdentification125Choice
from . import RestrictionStatus1Choice

class AdditiononalInformation13(base_types._BaseFieldType):

	__slots__ = ["_AcctVldtn", "_AddtlInf", "_Lmttn", "_Prd", "_Rgltr", "_Sts", "_Tp"]
	@property
	def AcctVldtn(self):
		return self._AcctVldtn

	@AcctVldtn.setter
	def AcctVldtn(self, value):
		self._AcctVldtn = value if value is not None else base_types.UninitialisedField(self, 'AcctVldtn', Max350Text, False)

	@AcctVldtn.deleter
	def AcctVldtn(self):
		del self._AcctVldtn
		self._AcctVldtn = base_types.UninitialisedField(self, 'AcctVldtn', Max350Text, False)

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max350Text, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max350Text, False)

	@property
	def Lmttn(self):
		return self._Lmttn

	@Lmttn.setter
	def Lmttn(self, value):
		self._Lmttn = value if value is not None else base_types.UninitialisedField(self, 'Lmttn', Max350Text, False)

	@Lmttn.deleter
	def Lmttn(self):
		del self._Lmttn
		self._Lmttn = base_types.UninitialisedField(self, 'Lmttn', Max350Text, False)

	@property
	def Prd(self):
		return self._Prd

	@Prd.setter
	def Prd(self, value):
		self._Prd = value if value is not None else base_types.UninitialisedField(self, 'Prd', DateTimePeriod2, False)

	@Prd.deleter
	def Prd(self):
		del self._Prd
		self._Prd = base_types.UninitialisedField(self, 'Prd', DateTimePeriod2, False)

	@property
	def Rgltr(self):
		return self._Rgltr

	@Rgltr.setter
	def Rgltr(self, value):
		self._Rgltr = value if value is not None else base_types.UninitialisedField(self, 'Rgltr', PartyIdentification125Choice, False)

	@Rgltr.deleter
	def Rgltr(self):
		del self._Rgltr
		self._Rgltr = base_types.UninitialisedField(self, 'Rgltr', PartyIdentification125Choice, False)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', RestrictionStatus1Choice, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', RestrictionStatus1Choice, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', Max35Text, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctVldtn', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lmttn', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prd', type=DateTimePeriod2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rgltr', type=PartyIdentification125Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=RestrictionStatus1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))