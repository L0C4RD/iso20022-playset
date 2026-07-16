# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DocumentLineIdentification1
from . import Max2048Text
from . import RemittanceAmount4

class DocumentLineInformation2(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Desc", "_Id"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', RemittanceAmount4, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', RemittanceAmount4, False)

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if value is not None else base_types.UninitialisedField(self, 'Desc', Max2048Text, False)

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = base_types.UninitialisedField(self, 'Desc', Max2048Text, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', DocumentLineIdentification1, True)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', DocumentLineIdentification1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=RemittanceAmount4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=DocumentLineIdentification1, min=1, max=None, mutex_group=None, array=True),
	))