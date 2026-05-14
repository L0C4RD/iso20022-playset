# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._PartyIdentificationAndAccount235 import PartyIdentificationAndAccount235

class DeliveringPartiesAndAccount24(base_types._BaseFieldType):

	__slots__ = ["_DlvrgAgtDtls", "_DlvrrsCtdnDtls", "_DlvrrsIntrmy1Dtls", "_DlvrrsIntrmy2Dtls"]
	@property
	def DlvrgAgtDtls(self):
		return self._DlvrgAgtDtls

	@DlvrgAgtDtls.setter
	def DlvrgAgtDtls(self, value):
		self._DlvrgAgtDtls = value if type(value) != base_types.auto else self.make_default("DlvrgAgtDtls")

	@DlvrgAgtDtls.deleter
	def DlvrgAgtDtls(self):
		del self._DlvrgAgtDtls
		self._DlvrgAgtDtls = None

	@property
	def DlvrrsCtdnDtls(self):
		return self._DlvrrsCtdnDtls

	@DlvrrsCtdnDtls.setter
	def DlvrrsCtdnDtls(self, value):
		self._DlvrrsCtdnDtls = value if type(value) != base_types.auto else self.make_default("DlvrrsCtdnDtls")

	@DlvrrsCtdnDtls.deleter
	def DlvrrsCtdnDtls(self):
		del self._DlvrrsCtdnDtls
		self._DlvrrsCtdnDtls = None

	@property
	def DlvrrsIntrmy1Dtls(self):
		return self._DlvrrsIntrmy1Dtls

	@DlvrrsIntrmy1Dtls.setter
	def DlvrrsIntrmy1Dtls(self, value):
		self._DlvrrsIntrmy1Dtls = value if type(value) != base_types.auto else self.make_default("DlvrrsIntrmy1Dtls")

	@DlvrrsIntrmy1Dtls.deleter
	def DlvrrsIntrmy1Dtls(self):
		del self._DlvrrsIntrmy1Dtls
		self._DlvrrsIntrmy1Dtls = None

	@property
	def DlvrrsIntrmy2Dtls(self):
		return self._DlvrrsIntrmy2Dtls

	@DlvrrsIntrmy2Dtls.setter
	def DlvrrsIntrmy2Dtls(self, value):
		self._DlvrrsIntrmy2Dtls = value if type(value) != base_types.auto else self.make_default("DlvrrsIntrmy2Dtls")

	@DlvrrsIntrmy2Dtls.deleter
	def DlvrrsIntrmy2Dtls(self):
		del self._DlvrrsIntrmy2Dtls
		self._DlvrrsIntrmy2Dtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DlvrgAgtDtls', type=PartyIdentificationAndAccount235, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvrrsCtdnDtls', type=PartyIdentificationAndAccount235, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvrrsIntrmy1Dtls', type=PartyIdentificationAndAccount235, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvrrsIntrmy2Dtls', type=PartyIdentificationAndAccount235, min=0, max=1, mutex_group=None, array=False),
	))