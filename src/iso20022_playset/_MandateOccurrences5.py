# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DatePeriod3
from . import Frequency36Choice
from . import ISODate
from . import SequenceType2Code

class MandateOccurrences5(base_types._BaseFieldType):

	__slots__ = ["_Drtn", "_FnlColltnDt", "_Frqcy", "_FrstColltnDt", "_SeqTp"]
	@property
	def Drtn(self):
		return self._Drtn

	@Drtn.setter
	def Drtn(self, value):
		self._Drtn = value if value is not None else base_types.UninitialisedField(self, 'Drtn', DatePeriod3, False)

	@Drtn.deleter
	def Drtn(self):
		del self._Drtn
		self._Drtn = base_types.UninitialisedField(self, 'Drtn', DatePeriod3, False)

	@property
	def FnlColltnDt(self):
		return self._FnlColltnDt

	@FnlColltnDt.setter
	def FnlColltnDt(self, value):
		self._FnlColltnDt = value if value is not None else base_types.UninitialisedField(self, 'FnlColltnDt', ISODate, False)

	@FnlColltnDt.deleter
	def FnlColltnDt(self):
		del self._FnlColltnDt
		self._FnlColltnDt = base_types.UninitialisedField(self, 'FnlColltnDt', ISODate, False)

	@property
	def Frqcy(self):
		return self._Frqcy

	@Frqcy.setter
	def Frqcy(self, value):
		self._Frqcy = value if value is not None else base_types.UninitialisedField(self, 'Frqcy', Frequency36Choice, False)

	@Frqcy.deleter
	def Frqcy(self):
		del self._Frqcy
		self._Frqcy = base_types.UninitialisedField(self, 'Frqcy', Frequency36Choice, False)

	@property
	def FrstColltnDt(self):
		return self._FrstColltnDt

	@FrstColltnDt.setter
	def FrstColltnDt(self, value):
		self._FrstColltnDt = value if value is not None else base_types.UninitialisedField(self, 'FrstColltnDt', ISODate, False)

	@FrstColltnDt.deleter
	def FrstColltnDt(self):
		del self._FrstColltnDt
		self._FrstColltnDt = base_types.UninitialisedField(self, 'FrstColltnDt', ISODate, False)

	@property
	def SeqTp(self):
		return self._SeqTp

	@SeqTp.setter
	def SeqTp(self, value):
		self._SeqTp = value if value is not None else base_types.UninitialisedField(self, 'SeqTp', SequenceType2Code, False)

	@SeqTp.deleter
	def SeqTp(self):
		del self._SeqTp
		self._SeqTp = base_types.UninitialisedField(self, 'SeqTp', SequenceType2Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Drtn', type=DatePeriod3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FnlColltnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frqcy', type=Frequency36Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrstColltnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeqTp', type=SequenceType2Code, min=1, max=1, mutex_group=None, array=False),
	))