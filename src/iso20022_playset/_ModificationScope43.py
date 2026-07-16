# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DataModification1Code
from . import ReferredAgent3

class ModificationScope43(base_types._BaseFieldType):

	__slots__ = ["_ModScpIndctn", "_Plcmnt"]
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
	def Plcmnt(self):
		return self._Plcmnt

	@Plcmnt.setter
	def Plcmnt(self, value):
		self._Plcmnt = value if value is not None else base_types.UninitialisedField(self, 'Plcmnt', ReferredAgent3, False)

	@Plcmnt.deleter
	def Plcmnt(self):
		del self._Plcmnt
		self._Plcmnt = base_types.UninitialisedField(self, 'Plcmnt', ReferredAgent3, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ModScpIndctn', type=DataModification1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Plcmnt', type=ReferredAgent3, min=1, max=1, mutex_group=None, array=False),
	))