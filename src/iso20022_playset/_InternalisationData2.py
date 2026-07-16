# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InternalisationDataVolume1

class InternalisationData2(base_types._BaseFieldType):

	__slots__ = ["_Faild", "_Sttld", "_Ttl"]
	@property
	def Faild(self):
		return self._Faild

	@Faild.setter
	def Faild(self, value):
		self._Faild = value if value is not None else base_types.UninitialisedField(self, 'Faild', InternalisationDataVolume1, False)

	@Faild.deleter
	def Faild(self):
		del self._Faild
		self._Faild = base_types.UninitialisedField(self, 'Faild', InternalisationDataVolume1, False)

	@property
	def Sttld(self):
		return self._Sttld

	@Sttld.setter
	def Sttld(self, value):
		self._Sttld = value if value is not None else base_types.UninitialisedField(self, 'Sttld', InternalisationDataVolume1, False)

	@Sttld.deleter
	def Sttld(self):
		del self._Sttld
		self._Sttld = base_types.UninitialisedField(self, 'Sttld', InternalisationDataVolume1, False)

	@property
	def Ttl(self):
		return self._Ttl

	@Ttl.setter
	def Ttl(self, value):
		self._Ttl = value if value is not None else base_types.UninitialisedField(self, 'Ttl', InternalisationDataVolume1, False)

	@Ttl.deleter
	def Ttl(self):
		del self._Ttl
		self._Ttl = base_types.UninitialisedField(self, 'Ttl', InternalisationDataVolume1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Faild', type=InternalisationDataVolume1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sttld', type=InternalisationDataVolume1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ttl', type=InternalisationDataVolume1, min=1, max=1, mutex_group=None, array=False),
	))