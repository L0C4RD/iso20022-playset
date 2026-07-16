# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import LimitIdentification8
from . import LimitIdentification9

class LimitIdentification3Choice(base_types._BaseFieldType):

	__slots__ = ["_AllCur", "_AllDflt", "_Cur", "_Dflt"]
	@property
	def AllCur(self):
		return self._AllCur

	@AllCur.setter
	def AllCur(self, value):
		self._AllCur = value if value is not None else base_types.UninitialisedField(self, 'AllCur', LimitIdentification9, False)

	@AllCur.deleter
	def AllCur(self):
		del self._AllCur
		self._AllCur = base_types.UninitialisedField(self, 'AllCur', LimitIdentification9, False)

	@property
	def AllDflt(self):
		return self._AllDflt

	@AllDflt.setter
	def AllDflt(self, value):
		self._AllDflt = value if value is not None else base_types.UninitialisedField(self, 'AllDflt', LimitIdentification9, False)

	@AllDflt.deleter
	def AllDflt(self):
		del self._AllDflt
		self._AllDflt = base_types.UninitialisedField(self, 'AllDflt', LimitIdentification9, False)

	@property
	def Cur(self):
		return self._Cur

	@Cur.setter
	def Cur(self, value):
		self._Cur = value if value is not None else base_types.UninitialisedField(self, 'Cur', LimitIdentification8, False)

	@Cur.deleter
	def Cur(self):
		del self._Cur
		self._Cur = base_types.UninitialisedField(self, 'Cur', LimitIdentification8, False)

	@property
	def Dflt(self):
		return self._Dflt

	@Dflt.setter
	def Dflt(self, value):
		self._Dflt = value if value is not None else base_types.UninitialisedField(self, 'Dflt', LimitIdentification8, False)

	@Dflt.deleter
	def Dflt(self):
		del self._Dflt
		self._Dflt = base_types.UninitialisedField(self, 'Dflt', LimitIdentification8, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AllCur', type=LimitIdentification9, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AllDflt', type=LimitIdentification9, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Cur', type=LimitIdentification8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Dflt', type=LimitIdentification8, min=0, max=1, mutex_group=1, array=False),
	))