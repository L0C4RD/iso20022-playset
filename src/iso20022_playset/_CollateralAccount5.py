# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MarginAccount1
from . import PartyIdentification118Choice
from . import TrueFalseIndicator

class CollateralAccount5(base_types._BaseFieldType):

	__slots__ = ["_CollSgrtnByVal", "_Id", "_RltdMrgnAcct", "_TitlTrfCollArrgmnt"]
	@property
	def CollSgrtnByVal(self):
		return self._CollSgrtnByVal

	@CollSgrtnByVal.setter
	def CollSgrtnByVal(self, value):
		self._CollSgrtnByVal = value if value is not None else base_types.UninitialisedField(self, 'CollSgrtnByVal', TrueFalseIndicator, False)

	@CollSgrtnByVal.deleter
	def CollSgrtnByVal(self):
		del self._CollSgrtnByVal
		self._CollSgrtnByVal = base_types.UninitialisedField(self, 'CollSgrtnByVal', TrueFalseIndicator, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', PartyIdentification118Choice, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', PartyIdentification118Choice, False)

	@property
	def RltdMrgnAcct(self):
		return self._RltdMrgnAcct

	@RltdMrgnAcct.setter
	def RltdMrgnAcct(self, value):
		self._RltdMrgnAcct = value if value is not None else base_types.UninitialisedField(self, 'RltdMrgnAcct', MarginAccount1, True)

	@RltdMrgnAcct.deleter
	def RltdMrgnAcct(self):
		del self._RltdMrgnAcct
		self._RltdMrgnAcct = base_types.UninitialisedField(self, 'RltdMrgnAcct', MarginAccount1, True)

	@property
	def TitlTrfCollArrgmnt(self):
		return self._TitlTrfCollArrgmnt

	@TitlTrfCollArrgmnt.setter
	def TitlTrfCollArrgmnt(self, value):
		self._TitlTrfCollArrgmnt = value if value is not None else base_types.UninitialisedField(self, 'TitlTrfCollArrgmnt', TrueFalseIndicator, False)

	@TitlTrfCollArrgmnt.deleter
	def TitlTrfCollArrgmnt(self):
		del self._TitlTrfCollArrgmnt
		self._TitlTrfCollArrgmnt = base_types.UninitialisedField(self, 'TitlTrfCollArrgmnt', TrueFalseIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollSgrtnByVal', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PartyIdentification118Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdMrgnAcct', type=MarginAccount1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TitlTrfCollArrgmnt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))