# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DataSetIdentification11
from . import ManagementPlanContent13
from . import Max9NumericText
from . import TrueFalseIndicator

class TerminalManagementDataSet34(base_types._BaseFieldType):

	__slots__ = ["_Cntt", "_Id", "_LastSeq", "_SeqCntr"]
	@property
	def Cntt(self):
		return self._Cntt

	@Cntt.setter
	def Cntt(self, value):
		self._Cntt = value if value is not None else base_types.UninitialisedField(self, 'Cntt', ManagementPlanContent13, False)

	@Cntt.deleter
	def Cntt(self):
		del self._Cntt
		self._Cntt = base_types.UninitialisedField(self, 'Cntt', ManagementPlanContent13, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', DataSetIdentification11, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', DataSetIdentification11, False)

	@property
	def LastSeq(self):
		return self._LastSeq

	@LastSeq.setter
	def LastSeq(self, value):
		self._LastSeq = value if value is not None else base_types.UninitialisedField(self, 'LastSeq', TrueFalseIndicator, False)

	@LastSeq.deleter
	def LastSeq(self):
		del self._LastSeq
		self._LastSeq = base_types.UninitialisedField(self, 'LastSeq', TrueFalseIndicator, False)

	@property
	def SeqCntr(self):
		return self._SeqCntr

	@SeqCntr.setter
	def SeqCntr(self, value):
		self._SeqCntr = value if value is not None else base_types.UninitialisedField(self, 'SeqCntr', Max9NumericText, False)

	@SeqCntr.deleter
	def SeqCntr(self):
		del self._SeqCntr
		self._SeqCntr = base_types.UninitialisedField(self, 'SeqCntr', Max9NumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cntt', type=ManagementPlanContent13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=DataSetIdentification11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LastSeq', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeqCntr', type=Max9NumericText, min=0, max=1, mutex_group=None, array=False),
	))