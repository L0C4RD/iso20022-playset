# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DocumentLineIdentification1 import DocumentLineIdentification1
from ._Max2048Text import Max2048Text
from ._RemittanceAmount4 import RemittanceAmount4

class DocumentLineInformation2(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Desc", "_Id"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != base_types.auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=RemittanceAmount4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=DocumentLineIdentification1, min=1, max=None, mutex_group=None, array=True),
	))