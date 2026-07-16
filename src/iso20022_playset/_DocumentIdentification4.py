# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BICIdentification1
from . import Max35Text
from . import Max3NumericText
from . import Number

class DocumentIdentification4(base_types._BaseFieldType):

	__slots__ = ["_DocIndx", "_Id", "_Submitr", "_Vrsn"]
	@property
	def DocIndx(self):
		return self._DocIndx

	@DocIndx.setter
	def DocIndx(self, value):
		self._DocIndx = value if value is not None else base_types.UninitialisedField(self, 'DocIndx', Max3NumericText, False)

	@DocIndx.deleter
	def DocIndx(self):
		del self._DocIndx
		self._DocIndx = base_types.UninitialisedField(self, 'DocIndx', Max3NumericText, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@property
	def Submitr(self):
		return self._Submitr

	@Submitr.setter
	def Submitr(self, value):
		self._Submitr = value if value is not None else base_types.UninitialisedField(self, 'Submitr', BICIdentification1, False)

	@Submitr.deleter
	def Submitr(self):
		del self._Submitr
		self._Submitr = base_types.UninitialisedField(self, 'Submitr', BICIdentification1, False)

	@property
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if value is not None else base_types.UninitialisedField(self, 'Vrsn', Number, False)

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = base_types.UninitialisedField(self, 'Vrsn', Number, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DocIndx', type=Max3NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Submitr', type=BICIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrsn', type=Number, min=1, max=1, mutex_group=None, array=False),
	))