# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import Party50Choice
from . import YesNoIndicator

class Case6(base_types._BaseFieldType):

	__slots__ = ["_Cretr", "_Id", "_ReopCaseIndctn"]
	@property
	def Cretr(self):
		return self._Cretr

	@Cretr.setter
	def Cretr(self, value):
		self._Cretr = value if value is not None else base_types.UninitialisedField(self, 'Cretr', Party50Choice, False)

	@Cretr.deleter
	def Cretr(self):
		del self._Cretr
		self._Cretr = base_types.UninitialisedField(self, 'Cretr', Party50Choice, False)

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
	def ReopCaseIndctn(self):
		return self._ReopCaseIndctn

	@ReopCaseIndctn.setter
	def ReopCaseIndctn(self, value):
		self._ReopCaseIndctn = value if value is not None else base_types.UninitialisedField(self, 'ReopCaseIndctn', YesNoIndicator, False)

	@ReopCaseIndctn.deleter
	def ReopCaseIndctn(self):
		del self._ReopCaseIndctn
		self._ReopCaseIndctn = base_types.UninitialisedField(self, 'ReopCaseIndctn', YesNoIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cretr', type=Party50Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReopCaseIndctn', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))