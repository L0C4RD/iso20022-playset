from . import base_types
from ._AttendanceAdmissionConditions2 import AttendanceAdmissionConditions2
from ._DateFormat58Choice import DateFormat58Choice
from ._Max350Text import Max350Text

class Attendance2(base_types._BaseFieldType):

	__slots__ = ["_AdmssnConds", "_ConfDdln", "_ConfInf", "_ConfMktDdln"]
	@property
	def AdmssnConds(self):
		return self._AdmssnConds

	@AdmssnConds.setter
	def AdmssnConds(self, value):
		self._AdmssnConds = value if type(value) != base_types.auto else self.make_default("AdmssnConds")

	@AdmssnConds.deleter
	def AdmssnConds(self):
		del self._AdmssnConds
		self._AdmssnConds = None

	@property
	def ConfDdln(self):
		return self._ConfDdln

	@ConfDdln.setter
	def ConfDdln(self, value):
		self._ConfDdln = value if type(value) != base_types.auto else self.make_default("ConfDdln")

	@ConfDdln.deleter
	def ConfDdln(self):
		del self._ConfDdln
		self._ConfDdln = None

	@property
	def ConfInf(self):
		return self._ConfInf

	@ConfInf.setter
	def ConfInf(self, value):
		self._ConfInf = value if type(value) != base_types.auto else self.make_default("ConfInf")

	@ConfInf.deleter
	def ConfInf(self):
		del self._ConfInf
		self._ConfInf = None

	@property
	def ConfMktDdln(self):
		return self._ConfMktDdln

	@ConfMktDdln.setter
	def ConfMktDdln(self, value):
		self._ConfMktDdln = value if type(value) != base_types.auto else self.make_default("ConfMktDdln")

	@ConfMktDdln.deleter
	def ConfMktDdln(self):
		del self._ConfMktDdln
		self._ConfMktDdln = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AdmssnConds', type=AttendanceAdmissionConditions2, min=0, max=7, mutex_group=None, array=True),
		base_types.FieldEntry(name='ConfDdln', type=DateFormat58Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConfInf', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConfMktDdln', type=DateFormat58Choice, min=0, max=1, mutex_group=None, array=False),
	))

