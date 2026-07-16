# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Amount4Choice
from . import Limit10
from . import Limit8
from . import LimitIdentification3Choice

class LimitStructure5(base_types._BaseFieldType):

	__slots__ = ["_LmtId", "_LmtValAmdmnt", "_NewLmtValSet", "_OdLmtValSet"]
	@property
	def LmtId(self):
		return self._LmtId

	@LmtId.setter
	def LmtId(self, value):
		self._LmtId = value if value is not None else base_types.UninitialisedField(self, 'LmtId', LimitIdentification3Choice, False)

	@LmtId.deleter
	def LmtId(self):
		del self._LmtId
		self._LmtId = base_types.UninitialisedField(self, 'LmtId', LimitIdentification3Choice, False)

	@property
	def LmtValAmdmnt(self):
		return self._LmtValAmdmnt

	@LmtValAmdmnt.setter
	def LmtValAmdmnt(self, value):
		self._LmtValAmdmnt = value if value is not None else base_types.UninitialisedField(self, 'LmtValAmdmnt', Amount4Choice, False)

	@LmtValAmdmnt.deleter
	def LmtValAmdmnt(self):
		del self._LmtValAmdmnt
		self._LmtValAmdmnt = base_types.UninitialisedField(self, 'LmtValAmdmnt', Amount4Choice, False)

	@property
	def NewLmtValSet(self):
		return self._NewLmtValSet

	@NewLmtValSet.setter
	def NewLmtValSet(self, value):
		self._NewLmtValSet = value if value is not None else base_types.UninitialisedField(self, 'NewLmtValSet', Limit8, False)

	@NewLmtValSet.deleter
	def NewLmtValSet(self):
		del self._NewLmtValSet
		self._NewLmtValSet = base_types.UninitialisedField(self, 'NewLmtValSet', Limit8, False)

	@property
	def OdLmtValSet(self):
		return self._OdLmtValSet

	@OdLmtValSet.setter
	def OdLmtValSet(self, value):
		self._OdLmtValSet = value if value is not None else base_types.UninitialisedField(self, 'OdLmtValSet', Limit10, False)

	@OdLmtValSet.deleter
	def OdLmtValSet(self):
		del self._OdLmtValSet
		self._OdLmtValSet = base_types.UninitialisedField(self, 'OdLmtValSet', Limit10, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='LmtId', type=LimitIdentification3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LmtValAmdmnt', type=Amount4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewLmtValSet', type=Limit8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OdLmtValSet', type=Limit10, min=0, max=1, mutex_group=None, array=False),
	))