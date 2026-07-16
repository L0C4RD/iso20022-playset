# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CitizenshipInformation2
from . import DataModification2Code

class ModificationScope39(base_types._BaseFieldType):

	__slots__ = ["_Ctznsh", "_ModScpIndctn"]
	@property
	def Ctznsh(self):
		return self._Ctznsh

	@Ctznsh.setter
	def Ctznsh(self, value):
		self._Ctznsh = value if value is not None else base_types.UninitialisedField(self, 'Ctznsh', CitizenshipInformation2, False)

	@Ctznsh.deleter
	def Ctznsh(self):
		del self._Ctznsh
		self._Ctznsh = base_types.UninitialisedField(self, 'Ctznsh', CitizenshipInformation2, False)

	@property
	def ModScpIndctn(self):
		return self._ModScpIndctn

	@ModScpIndctn.setter
	def ModScpIndctn(self, value):
		self._ModScpIndctn = value if value is not None else base_types.UninitialisedField(self, 'ModScpIndctn', DataModification2Code, False)

	@ModScpIndctn.deleter
	def ModScpIndctn(self):
		del self._ModScpIndctn
		self._ModScpIndctn = base_types.UninitialisedField(self, 'ModScpIndctn', DataModification2Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ctznsh', type=CitizenshipInformation2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModScpIndctn', type=DataModification2Code, min=1, max=1, mutex_group=None, array=False),
	))