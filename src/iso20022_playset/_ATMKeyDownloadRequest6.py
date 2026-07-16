# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMCommand15
from . import ATMCommand16
from . import ATMEnvironment15
from . import ATMSecurityContext3
from . import Max140Binary
from . import SecurityParameters18

class ATMKeyDownloadRequest6(base_types._BaseFieldType):

	__slots__ = ["_ATMSctyCntxt", "_ATMSctyParams", "_CmdCntxt", "_CmdRslt", "_Envt", "_HstChllng"]
	@property
	def ATMSctyCntxt(self):
		return self._ATMSctyCntxt

	@ATMSctyCntxt.setter
	def ATMSctyCntxt(self, value):
		self._ATMSctyCntxt = value if value is not None else base_types.UninitialisedField(self, 'ATMSctyCntxt', ATMSecurityContext3, False)

	@ATMSctyCntxt.deleter
	def ATMSctyCntxt(self):
		del self._ATMSctyCntxt
		self._ATMSctyCntxt = base_types.UninitialisedField(self, 'ATMSctyCntxt', ATMSecurityContext3, False)

	@property
	def ATMSctyParams(self):
		return self._ATMSctyParams

	@ATMSctyParams.setter
	def ATMSctyParams(self, value):
		self._ATMSctyParams = value if value is not None else base_types.UninitialisedField(self, 'ATMSctyParams', SecurityParameters18, False)

	@ATMSctyParams.deleter
	def ATMSctyParams(self):
		del self._ATMSctyParams
		self._ATMSctyParams = base_types.UninitialisedField(self, 'ATMSctyParams', SecurityParameters18, False)

	@property
	def CmdCntxt(self):
		return self._CmdCntxt

	@CmdCntxt.setter
	def CmdCntxt(self, value):
		self._CmdCntxt = value if value is not None else base_types.UninitialisedField(self, 'CmdCntxt', ATMCommand16, False)

	@CmdCntxt.deleter
	def CmdCntxt(self):
		del self._CmdCntxt
		self._CmdCntxt = base_types.UninitialisedField(self, 'CmdCntxt', ATMCommand16, False)

	@property
	def CmdRslt(self):
		return self._CmdRslt

	@CmdRslt.setter
	def CmdRslt(self, value):
		self._CmdRslt = value if value is not None else base_types.UninitialisedField(self, 'CmdRslt', ATMCommand15, True)

	@CmdRslt.deleter
	def CmdRslt(self):
		del self._CmdRslt
		self._CmdRslt = base_types.UninitialisedField(self, 'CmdRslt', ATMCommand15, True)

	@property
	def Envt(self):
		return self._Envt

	@Envt.setter
	def Envt(self, value):
		self._Envt = value if value is not None else base_types.UninitialisedField(self, 'Envt', ATMEnvironment15, False)

	@Envt.deleter
	def Envt(self):
		del self._Envt
		self._Envt = base_types.UninitialisedField(self, 'Envt', ATMEnvironment15, False)

	@property
	def HstChllng(self):
		return self._HstChllng

	@HstChllng.setter
	def HstChllng(self, value):
		self._HstChllng = value if value is not None else base_types.UninitialisedField(self, 'HstChllng', Max140Binary, False)

	@HstChllng.deleter
	def HstChllng(self):
		del self._HstChllng
		self._HstChllng = base_types.UninitialisedField(self, 'HstChllng', Max140Binary, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ATMSctyCntxt', type=ATMSecurityContext3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ATMSctyParams', type=SecurityParameters18, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmdCntxt', type=ATMCommand16, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmdRslt', type=ATMCommand15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Envt', type=ATMEnvironment15, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HstChllng', type=Max140Binary, min=0, max=1, mutex_group=None, array=False),
	))