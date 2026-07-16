# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMCommand17
from . import ATMEnvironment7
from . import ATMSecurityContext3
from . import Max140Binary
from . import SecurityParameters10

class ATMKeyDownloadResponse5(base_types._BaseFieldType):

	__slots__ = ["_ATMChllng", "_ATMSctyCntxt", "_Cmd", "_Envt", "_HstSctyParams"]
	@property
	def ATMChllng(self):
		return self._ATMChllng

	@ATMChllng.setter
	def ATMChllng(self, value):
		self._ATMChllng = value if value is not None else base_types.UninitialisedField(self, 'ATMChllng', Max140Binary, False)

	@ATMChllng.deleter
	def ATMChllng(self):
		del self._ATMChllng
		self._ATMChllng = base_types.UninitialisedField(self, 'ATMChllng', Max140Binary, False)

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
	def Cmd(self):
		return self._Cmd

	@Cmd.setter
	def Cmd(self, value):
		self._Cmd = value if value is not None else base_types.UninitialisedField(self, 'Cmd', ATMCommand17, True)

	@Cmd.deleter
	def Cmd(self):
		del self._Cmd
		self._Cmd = base_types.UninitialisedField(self, 'Cmd', ATMCommand17, True)

	@property
	def Envt(self):
		return self._Envt

	@Envt.setter
	def Envt(self, value):
		self._Envt = value if value is not None else base_types.UninitialisedField(self, 'Envt', ATMEnvironment7, False)

	@Envt.deleter
	def Envt(self):
		del self._Envt
		self._Envt = base_types.UninitialisedField(self, 'Envt', ATMEnvironment7, False)

	@property
	def HstSctyParams(self):
		return self._HstSctyParams

	@HstSctyParams.setter
	def HstSctyParams(self, value):
		self._HstSctyParams = value if value is not None else base_types.UninitialisedField(self, 'HstSctyParams', SecurityParameters10, False)

	@HstSctyParams.deleter
	def HstSctyParams(self):
		del self._HstSctyParams
		self._HstSctyParams = base_types.UninitialisedField(self, 'HstSctyParams', SecurityParameters10, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ATMChllng', type=Max140Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ATMSctyCntxt', type=ATMSecurityContext3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cmd', type=ATMCommand17, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Envt', type=ATMEnvironment7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HstSctyParams', type=SecurityParameters10, min=1, max=1, mutex_group=None, array=False),
	))