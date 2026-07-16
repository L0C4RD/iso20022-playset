# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DocumentType1Choice
from . import Max500Text

class ContractReference1(base_types._BaseFieldType):

	__slots__ = ["_Ref", "_Tp"]
	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if value is not None else base_types.UninitialisedField(self, 'Ref', Max500Text, False)

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = base_types.UninitialisedField(self, 'Ref', Max500Text, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', DocumentType1Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', DocumentType1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ref', type=Max500Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=DocumentType1Choice, min=0, max=1, mutex_group=None, array=False),
	))