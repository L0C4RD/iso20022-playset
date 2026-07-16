# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DataModification1Code
from . import DocumentToSend4

class ModificationScope44(base_types._BaseFieldType):

	__slots__ = ["_ModScpIndctn", "_SvcLvlAgrmt"]
	@property
	def ModScpIndctn(self):
		return self._ModScpIndctn

	@ModScpIndctn.setter
	def ModScpIndctn(self, value):
		self._ModScpIndctn = value if value is not None else base_types.UninitialisedField(self, 'ModScpIndctn', DataModification1Code, False)

	@ModScpIndctn.deleter
	def ModScpIndctn(self):
		del self._ModScpIndctn
		self._ModScpIndctn = base_types.UninitialisedField(self, 'ModScpIndctn', DataModification1Code, False)

	@property
	def SvcLvlAgrmt(self):
		return self._SvcLvlAgrmt

	@SvcLvlAgrmt.setter
	def SvcLvlAgrmt(self, value):
		self._SvcLvlAgrmt = value if value is not None else base_types.UninitialisedField(self, 'SvcLvlAgrmt', DocumentToSend4, False)

	@SvcLvlAgrmt.deleter
	def SvcLvlAgrmt(self):
		del self._SvcLvlAgrmt
		self._SvcLvlAgrmt = base_types.UninitialisedField(self, 'SvcLvlAgrmt', DocumentToSend4, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ModScpIndctn', type=DataModification1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcLvlAgrmt', type=DocumentToSend4, min=1, max=1, mutex_group=None, array=False),
	))