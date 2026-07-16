# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AttendanceAdmissionConditions2
from . import DateFormat58Choice
from . import Max350Text

class Attendance2(base_types._BaseFieldType):

	__slots__ = ["_AdmssnConds", "_ConfDdln", "_ConfInf", "_ConfMktDdln"]
	@property
	def AdmssnConds(self):
		return self._AdmssnConds

	@AdmssnConds.setter
	def AdmssnConds(self, value):
		self._AdmssnConds = value if value is not None else base_types.UninitialisedField(self, 'AdmssnConds', AttendanceAdmissionConditions2, True)

	@AdmssnConds.deleter
	def AdmssnConds(self):
		del self._AdmssnConds
		self._AdmssnConds = base_types.UninitialisedField(self, 'AdmssnConds', AttendanceAdmissionConditions2, True)

	@property
	def ConfDdln(self):
		return self._ConfDdln

	@ConfDdln.setter
	def ConfDdln(self, value):
		self._ConfDdln = value if value is not None else base_types.UninitialisedField(self, 'ConfDdln', DateFormat58Choice, False)

	@ConfDdln.deleter
	def ConfDdln(self):
		del self._ConfDdln
		self._ConfDdln = base_types.UninitialisedField(self, 'ConfDdln', DateFormat58Choice, False)

	@property
	def ConfInf(self):
		return self._ConfInf

	@ConfInf.setter
	def ConfInf(self, value):
		self._ConfInf = value if value is not None else base_types.UninitialisedField(self, 'ConfInf', Max350Text, False)

	@ConfInf.deleter
	def ConfInf(self):
		del self._ConfInf
		self._ConfInf = base_types.UninitialisedField(self, 'ConfInf', Max350Text, False)

	@property
	def ConfMktDdln(self):
		return self._ConfMktDdln

	@ConfMktDdln.setter
	def ConfMktDdln(self, value):
		self._ConfMktDdln = value if value is not None else base_types.UninitialisedField(self, 'ConfMktDdln', DateFormat58Choice, False)

	@ConfMktDdln.deleter
	def ConfMktDdln(self):
		del self._ConfMktDdln
		self._ConfMktDdln = base_types.UninitialisedField(self, 'ConfMktDdln', DateFormat58Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AdmssnConds', type=AttendanceAdmissionConditions2, min=0, max=7, mutex_group=None, array=True),
		base_types.FieldEntry(name='ConfDdln', type=DateFormat58Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConfInf', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConfMktDdln', type=DateFormat58Choice, min=0, max=1, mutex_group=None, array=False),
	))