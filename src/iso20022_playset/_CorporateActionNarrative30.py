# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max350Text

class CorporateActionNarrative30(base_types._BaseFieldType):

	__slots__ = ["_CertfctnBrkdwn", "_PtyCtctNrrtv", "_RegnDtls"]
	@property
	def CertfctnBrkdwn(self):
		return self._CertfctnBrkdwn

	@CertfctnBrkdwn.setter
	def CertfctnBrkdwn(self, value):
		self._CertfctnBrkdwn = value if value is not None else base_types.UninitialisedField(self, 'CertfctnBrkdwn', Max350Text, True)

	@CertfctnBrkdwn.deleter
	def CertfctnBrkdwn(self):
		del self._CertfctnBrkdwn
		self._CertfctnBrkdwn = base_types.UninitialisedField(self, 'CertfctnBrkdwn', Max350Text, True)

	@property
	def PtyCtctNrrtv(self):
		return self._PtyCtctNrrtv

	@PtyCtctNrrtv.setter
	def PtyCtctNrrtv(self, value):
		self._PtyCtctNrrtv = value if value is not None else base_types.UninitialisedField(self, 'PtyCtctNrrtv', Max350Text, True)

	@PtyCtctNrrtv.deleter
	def PtyCtctNrrtv(self):
		del self._PtyCtctNrrtv
		self._PtyCtctNrrtv = base_types.UninitialisedField(self, 'PtyCtctNrrtv', Max350Text, True)

	@property
	def RegnDtls(self):
		return self._RegnDtls

	@RegnDtls.setter
	def RegnDtls(self, value):
		self._RegnDtls = value if value is not None else base_types.UninitialisedField(self, 'RegnDtls', Max350Text, True)

	@RegnDtls.deleter
	def RegnDtls(self):
		del self._RegnDtls
		self._RegnDtls = base_types.UninitialisedField(self, 'RegnDtls', Max350Text, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CertfctnBrkdwn', type=Max350Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PtyCtctNrrtv', type=Max350Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RegnDtls', type=Max350Text, min=0, max=None, mutex_group=None, array=True),
	))