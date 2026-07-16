# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CSCManagement1Code
from . import Min3Max4NumericText

class CardSecurityInformation1(base_types._BaseFieldType):

	__slots__ = ["_CSCMgmt", "_CSCVal"]
	@property
	def CSCMgmt(self):
		return self._CSCMgmt

	@CSCMgmt.setter
	def CSCMgmt(self, value):
		self._CSCMgmt = value if value is not None else base_types.UninitialisedField(self, 'CSCMgmt', CSCManagement1Code, False)

	@CSCMgmt.deleter
	def CSCMgmt(self):
		del self._CSCMgmt
		self._CSCMgmt = base_types.UninitialisedField(self, 'CSCMgmt', CSCManagement1Code, False)

	@property
	def CSCVal(self):
		return self._CSCVal

	@CSCVal.setter
	def CSCVal(self, value):
		self._CSCVal = value if value is not None else base_types.UninitialisedField(self, 'CSCVal', Min3Max4NumericText, False)

	@CSCVal.deleter
	def CSCVal(self):
		del self._CSCVal
		self._CSCVal = base_types.UninitialisedField(self, 'CSCVal', Min3Max4NumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CSCMgmt', type=CSCManagement1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CSCVal', type=Min3Max4NumericText, min=0, max=1, mutex_group=None, array=False),
	))