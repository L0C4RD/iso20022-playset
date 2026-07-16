# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DetailedAmount21
from . import ISODateTime
from . import Number

class AggregationTransaction3(base_types._BaseFieldType):

	__slots__ = ["_FrstPmtDtTm", "_IndvPmt", "_LastPmtDtTm", "_NbOfPmts"]
	@property
	def FrstPmtDtTm(self):
		return self._FrstPmtDtTm

	@FrstPmtDtTm.setter
	def FrstPmtDtTm(self, value):
		self._FrstPmtDtTm = value if value is not None else base_types.UninitialisedField(self, 'FrstPmtDtTm', ISODateTime, False)

	@FrstPmtDtTm.deleter
	def FrstPmtDtTm(self):
		del self._FrstPmtDtTm
		self._FrstPmtDtTm = base_types.UninitialisedField(self, 'FrstPmtDtTm', ISODateTime, False)

	@property
	def IndvPmt(self):
		return self._IndvPmt

	@IndvPmt.setter
	def IndvPmt(self, value):
		self._IndvPmt = value if value is not None else base_types.UninitialisedField(self, 'IndvPmt', DetailedAmount21, True)

	@IndvPmt.deleter
	def IndvPmt(self):
		del self._IndvPmt
		self._IndvPmt = base_types.UninitialisedField(self, 'IndvPmt', DetailedAmount21, True)

	@property
	def LastPmtDtTm(self):
		return self._LastPmtDtTm

	@LastPmtDtTm.setter
	def LastPmtDtTm(self, value):
		self._LastPmtDtTm = value if value is not None else base_types.UninitialisedField(self, 'LastPmtDtTm', ISODateTime, False)

	@LastPmtDtTm.deleter
	def LastPmtDtTm(self):
		del self._LastPmtDtTm
		self._LastPmtDtTm = base_types.UninitialisedField(self, 'LastPmtDtTm', ISODateTime, False)

	@property
	def NbOfPmts(self):
		return self._NbOfPmts

	@NbOfPmts.setter
	def NbOfPmts(self, value):
		self._NbOfPmts = value if value is not None else base_types.UninitialisedField(self, 'NbOfPmts', Number, False)

	@NbOfPmts.deleter
	def NbOfPmts(self):
		del self._NbOfPmts
		self._NbOfPmts = base_types.UninitialisedField(self, 'NbOfPmts', Number, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FrstPmtDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndvPmt', type=DetailedAmount21, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LastPmtDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfPmts', type=Number, min=0, max=1, mutex_group=None, array=False),
	))