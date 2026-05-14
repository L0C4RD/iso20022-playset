# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DetailedAmount21 import DetailedAmount21
from ._ISODateTime import ISODateTime
from ._Number import Number

class AggregationTransaction3(base_types._BaseFieldType):

	__slots__ = ["_FrstPmtDtTm", "_IndvPmt", "_LastPmtDtTm", "_NbOfPmts"]
	@property
	def FrstPmtDtTm(self):
		return self._FrstPmtDtTm

	@FrstPmtDtTm.setter
	def FrstPmtDtTm(self, value):
		self._FrstPmtDtTm = value if type(value) != base_types.auto else self.make_default("FrstPmtDtTm")

	@FrstPmtDtTm.deleter
	def FrstPmtDtTm(self):
		del self._FrstPmtDtTm
		self._FrstPmtDtTm = None

	@property
	def IndvPmt(self):
		return self._IndvPmt

	@IndvPmt.setter
	def IndvPmt(self, value):
		self._IndvPmt = value if type(value) != base_types.auto else self.make_default("IndvPmt")

	@IndvPmt.deleter
	def IndvPmt(self):
		del self._IndvPmt
		self._IndvPmt = None

	@property
	def LastPmtDtTm(self):
		return self._LastPmtDtTm

	@LastPmtDtTm.setter
	def LastPmtDtTm(self, value):
		self._LastPmtDtTm = value if type(value) != base_types.auto else self.make_default("LastPmtDtTm")

	@LastPmtDtTm.deleter
	def LastPmtDtTm(self):
		del self._LastPmtDtTm
		self._LastPmtDtTm = None

	@property
	def NbOfPmts(self):
		return self._NbOfPmts

	@NbOfPmts.setter
	def NbOfPmts(self, value):
		self._NbOfPmts = value if type(value) != base_types.auto else self.make_default("NbOfPmts")

	@NbOfPmts.deleter
	def NbOfPmts(self):
		del self._NbOfPmts
		self._NbOfPmts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FrstPmtDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndvPmt', type=DetailedAmount21, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LastPmtDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfPmts', type=Number, min=0, max=1, mutex_group=None, array=False),
	))