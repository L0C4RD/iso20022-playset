# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max10KBinary
from . import Max140Binary
from . import TMSAction13

class ManagementPlanContent13(base_types._BaseFieldType):

	__slots__ = ["_Actn", "_KeyNcphrmntCert", "_TMChllng"]
	@property
	def Actn(self):
		return self._Actn

	@Actn.setter
	def Actn(self, value):
		self._Actn = value if value is not None else base_types.UninitialisedField(self, 'Actn', TMSAction13, True)

	@Actn.deleter
	def Actn(self):
		del self._Actn
		self._Actn = base_types.UninitialisedField(self, 'Actn', TMSAction13, True)

	@property
	def KeyNcphrmntCert(self):
		return self._KeyNcphrmntCert

	@KeyNcphrmntCert.setter
	def KeyNcphrmntCert(self, value):
		self._KeyNcphrmntCert = value if value is not None else base_types.UninitialisedField(self, 'KeyNcphrmntCert', Max10KBinary, True)

	@KeyNcphrmntCert.deleter
	def KeyNcphrmntCert(self):
		del self._KeyNcphrmntCert
		self._KeyNcphrmntCert = base_types.UninitialisedField(self, 'KeyNcphrmntCert', Max10KBinary, True)

	@property
	def TMChllng(self):
		return self._TMChllng

	@TMChllng.setter
	def TMChllng(self, value):
		self._TMChllng = value if value is not None else base_types.UninitialisedField(self, 'TMChllng', Max140Binary, False)

	@TMChllng.deleter
	def TMChllng(self):
		del self._TMChllng
		self._TMChllng = base_types.UninitialisedField(self, 'TMChllng', Max140Binary, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Actn', type=TMSAction13, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='KeyNcphrmntCert', type=Max10KBinary, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TMChllng', type=Max140Binary, min=0, max=1, mutex_group=None, array=False),
	))